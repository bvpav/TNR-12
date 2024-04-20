#pragma once

#define MIN_PULSE 46
#define MID_PULSE 95
#define MAX_PULSE 144

struct DualSense
{
  DualSense(bd_addr_t mac);

  void on_connected(ControllerPtr ctl);

  void on_disconnected(ControllerPtr ctl);

  void update();

  bool drum_enabled = false;

  int32_t throttle_l = 0; // -1023 - 1023
  int32_t throttle_r = 0; // -1023 - 1023

private:
  ControllerPtr m_ctl = nullptr;
  bool m_drum_locked = false, m_lock_processed = false;
  int64_t m_lock_pressed_at = -1;
  bool m_drum_pressed_prev = false;
  bool m_lock_previous_pressed = false;
};