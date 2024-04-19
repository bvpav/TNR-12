#include <Bluepad32.h>
#include <uni.h>

struct DualSense
{
  DualSense(bd_addr_t mac);

  void on_connected(ControllerPtr ctl);

  void on_disconnected(ControllerPtr ctl);

  void update();

private:
  ControllerPtr m_ctl = nullptr;
};

bd_addr_t DUALSENSE_MAC = {0x4C, 0xB9, 0x9B, 0x05, 0xD2, 0x83};

DualSense ds(DUALSENSE_MAC);

void on_connected_callback(ControllerPtr ctl)    { ds.on_connected(ctl); }
void on_disconnected_callback(ControllerPtr ctl) { ds.on_disconnected(ctl); }

void setup()
{
  uni_bt_allowlist_set_enabled(true);
  Serial.begin(115200);
  BP32.setup(on_connected_callback, on_disconnected_callback);
  // BP32.forgetBluetoothKeys();
  BP32.enableVirtualDevice(false);
}

void loop()
{
  if (BP32.update())
  {
    ds.update();
  }
  vTaskDelay(1);
}
