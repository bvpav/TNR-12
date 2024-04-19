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
  Serial.printf(
      "idx=%d, dpad: 0x%02x, buttons: 0x%04x, axis L: %4d, %4d, axis R: %4d, %4d, brake: %4d, throttle: %4d, "
      "misc: 0x%02x, gyro x:%6d y:%6d z:%6d, accel x:%6d y:%6d z:%6d\n",
      m_ctl->index(),        // Controller Index
      m_ctl->dpad(),         // D-pad
      m_ctl->buttons(),      // bitmask of pressed buttons
      m_ctl->axisX(),        // (-511 - 512) left X Axis
      m_ctl->axisY(),        // (-511 - 512) left Y axis
      m_ctl->axisRX(),       // (-511 - 512) right X axis
      m_ctl->axisRY(),       // (-511 - 512) right Y axis
      m_ctl->brake(),        // (0 - 1023): brake button
      m_ctl->throttle(),     // (0 - 1023): throttle (AKA gas) button
      m_ctl->miscButtons(),  // bitmask of pressed "misc" buttons
      m_ctl->gyroX(),        // Gyro X
      m_ctl->gyroY(),        // Gyro Y
      m_ctl->gyroZ(),        // Gyro Z
      m_ctl->accelX(),       // Accelerometer X
      m_ctl->accelY(),       // Accelerometer Y
      m_ctl->accelZ()        // Accelerometer Z
  );
}