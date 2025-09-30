# 2025-09-30T15:42:32.345773700
import vitis

client = vitis.create_client()
client.set_workspace(path="vitis6")

platform = client.get_component(name="psoc_platform")
status = platform.build()

comp = client.get_component(name="hello_world")
comp.build()

vitis.dispose()

