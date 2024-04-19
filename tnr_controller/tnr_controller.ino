#include <Bluepad32.h>
#include <ESP32Servo.h>
#include <uni.h>

#include "tnr_dualsense.h"

bd_addr_t DUALSENSE_MAC = {0x4C, 0xB9, 0x9B, 0x05, 0xD2, 0x83};

DualSense ds(DUALSENSE_MAC);
Servo esc;

void on_connected_callback(ControllerPtr ctl)    { ds.on_connected(ctl); }
void on_disconnected_callback(ControllerPtr ctl) { ds.on_disconnected(ctl); }

void setup()
{
  uni_bt_allowlist_set_enabled(true);
  
  Serial.begin(115200);

  esc.attach(12);

  BP32.setup(on_connected_callback, on_disconnected_callback);
  BP32.enableVirtualDevice(false);
}

void loop()
{
  if (BP32.update())
    ds.update();

  if (ds.drum_enabled)
    esc.write(MID_PULSE);
  else
    esc.write(MIN_PULSE);

  vTaskDelay(1);
}
