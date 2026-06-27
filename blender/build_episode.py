import bpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "renders"
OUTPUT.mkdir(exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100
scene.render.fps = 24

# Starter camera
bpy.ops.object.camera_add(location=(0, -10, 5), rotation=(1.15, 0, 0))
scene.camera = bpy.context.object

# Ground
bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))

# Placeholder Dino body
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 1.5), scale=(1.1, 0.8, 1.3))
dino = bpy.context.object
dino.name = "Dino_PLACEHOLDER"

# Lighting
bpy.ops.object.light_add(type="AREA", location=(3, -4, 7))
bpy.context.object.data.energy = 1200
bpy.context.object.data.shape = "DISK"
bpy.context.object.data.size = 5

scene.frame_start = 1
scene.frame_end = 120
scene.render.filepath = str(OUTPUT / "starter_scene.mp4")
scene.render.image_settings.file_format = "FFMPEG"
scene.render.ffmpeg.format = "MPEG4"
scene.render.ffmpeg.codec = "H264"

bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / "dino_starter.blend"))
print("Starter Blender project created.")
