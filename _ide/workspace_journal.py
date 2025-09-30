# 2025-09-30T16:56:22.267304100
import vitis

client = vitis.create_client()
client.set_workspace(path="vitis6")

platform = client.get_component(name="psoc_platform")
status = platform.update_hw(hw_design = "L:\Dokumente\psoc\psoc-zynq\hw\fpga_soc_top.xsa")

status = platform.build()

comp = client.get_component(name="hello_world")
comp.build()

