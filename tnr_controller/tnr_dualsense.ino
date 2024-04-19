#include <Bluepad32.h>
#include <uni.h>

DualSense::DualSense(bd_addr_t mac)
{
  uni_bt_allowlist_add_addr(mac);
}

void DualSense::on_connected(ControllerPtr ctl)
{
  if (m_ctl == nullptr)
    m_ctl = ctl;
}

void DualSense::on_disconnected(ControllerPtr ctl)
{
  if (ctl != m_ctl)
    return;
  m_ctl = nullptr;
}

void DualSense::update()
{
  if (!m_ctl || !m_ctl->isConnected() || !m_ctl->hasData())
    return;

  if (m_ctl->x())
  {
    if (m_drum_locked)
      m_ctl->playDualRumble(0, 100, 0x40, drum_enabled ? 0x50 : 0xcc);
    else
    {
      drum_enabled = !drum_enabled;
      if (drum_enabled)
        m_ctl->setColorLED(0xff, 0x00, 0x00);
      else
        m_ctl->setColorLED(0x00, 0x00, 0xff);
    }
  }

  bool lock_pressed = m_ctl->l1();
  if (lock_pressed)
  {
    int64_t now = esp_timer_get_time();
    if (!m_lock_previous_pressed)
      m_lock_pressed_at = now, m_lock_processed = false;
    if (now - m_lock_pressed_at >= 1000000 && !m_lock_processed)
    {
      m_drum_locked = !m_drum_locked;
      m_ctl->playDualRumble(0, 1000, 0xaa, 0xff);
      m_ctl->setPlayerLEDs(m_drum_locked ? 1 : 3);
      m_lock_processed = true;
    }
  }
  m_lock_previous_pressed = lock_pressed;

  throttle = map(m_ctl->throttle(), 0, 1020, MID_PULSE, MAX_PULSE);
}