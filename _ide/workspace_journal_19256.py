# 2025-09-30T13:30:51.697482100
import vitis

client = vitis.create_client()
client.set_workspace(path="vitis6")

advanced_options = client.create_advanced_options_dict(dt_overlay="0")

platform = client.create_platform_component(name = "psoc_platform",hw_design = "L:\Dokumente\psoc\psoc-zynq\hw\fpga_soc_top.xsa",os = "standalone",cpu = "ps7_cortexa9_0",domain_name = "standalone_ps7_cortexa9_0",generate_dtb = False,advanced_options = advanced_options,compiler = "gcc")

platform = client.get_component(name="psoc_platform")
status = platform.update_desc(desc="")

comp = client.create_app_component(name="blink_led",platform = "$COMPONENT_LOCATION/../psoc_platform/export/psoc_platform/psoc_platform.xpfm",domain = "standalone_ps7_cortexa9_0",template = "hello_world")

status = platform.build()

comp = client.get_component(name="blink_led")
comp.build()

status = platform.update_hw(hw_design = "L:\Dokumente\psoc\psoc-zynq\hw\fpga_soc_top.xsa")

client.delete_component(name="blink_led")

client.delete_component(name="psoc_platform")

client.delete_component(name="psoc_platform")

advanced_options = client.create_advanced_options_dict(dt_overlay="0")

platform = client.create_platform_component(name = "psoc_platform",hw_design = "L:\Dokumente\psoc\psoc-zynq\hw\fpga_soc_top.xsa",os = "standalone",cpu = "ps7_cortexa9_0",domain_name = "standalone_ps7_cortexa9_0",generate_dtb = False,advanced_options = advanced_options,compiler = "gcc")

comp = client.create_app_component(name="hello_world",platform = "$COMPONENT_LOCATION/../psoc_platform/export/psoc_platform/psoc_platform.xpfm",domain = "standalone_ps7_cortexa9_0",template = "hello_world")

status = platform.build()

comp = client.get_component(name="hello_world")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

vitis.dispose()

