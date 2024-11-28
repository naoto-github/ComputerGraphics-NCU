import bpy
import math

# 新しいメッシュデータを作成
mesh = bpy.data.meshes.new("MyMesh")

length = 2
angle = 72

vertices = []

for i in range(6):
    v = (2 * math.cos(math.radians(angle * i + 90)), 2 * math.sin(math.radians(angle * i + 90)), 0)
    vertices.append(v)

# 各面の頂点インデックスを整理
faces = [
    (0, 1, 2, 3, 4, 5)
]

# メッシュに頂点を追加
mesh.from_pydata(vertices, [], faces)

# メッシュを更新
mesh.update()

# 新しいオブジェクトをシーンにリンク（追加）
obj = bpy.data.objects.new("Pentagon", mesh)
bpy.context.collection.objects.link(obj)