import bpy, json, math
from pathlib import Path
from mathutils import Vector
P=Path(__file__).parent;O=P if (P/'ACTIVATION_SURFACE_DATA.json').exists() else P/'publication_010'
D=json.loads((O/'ACTIVATION_SURFACE_DATA.json').read_text())
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene;scene.render.engine='BLENDER_EEVEE_NEXT'
scene.render.resolution_x=1900;scene.render.resolution_y=1350;scene.render.resolution_percentage=100
scene.world.color=(0.8,0.8,0.8);scene.render.image_settings.file_format='PNG'
scene.view_settings.view_transform='Standard'
def mat(name,color,alpha=1):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,alpha);m.use_nodes=True
 nodes=m.node_tree.nodes;nodes.clear();out=nodes.new('ShaderNodeOutputMaterial');em=nodes.new('ShaderNodeEmission');em.inputs[0].default_value=(*color,1);em.inputs[1].default_value=1
 tr=nodes.new('ShaderNodeBsdfTransparent');mx=nodes.new('ShaderNodeMixShader');mx.inputs[0].default_value=alpha;m.node_tree.links.new(tr.outputs[0],mx.inputs[1]);m.node_tree.links.new(em.outputs[0],mx.inputs[2]);m.node_tree.links.new(mx.outputs[0],out.inputs[0])
 if alpha<1:m.surface_render_method='DITHERED'
 return m
navy=mat('Axes and labels',(0.025,.075,.14));blue=mat('Threshold surface',(.06,.48,.61),.88)
orange=mat('High-cutoff edge',(.9,.32,.08));dark=mat('Low-cutoff edge',(.08,.22,.42));gray=mat('Grid',(.53,.61,.68))
plane=mat('Fixed heat exponent',(.95,.62,.16),.16);yellow=mat('Transition line',(.95,.28,.05))
def curve(name,pts,material,width=.01):
 data=bpy.data.curves.new(name,'CURVE');data.dimensions='3D';data.bevel_depth=width;data.bevel_resolution=2
 spl=data.splines.new('POLY');spl.points.add(len(pts)-1)
 for pp,co in zip(spl.points,pts):pp.co=(*co,1)
 ob=bpy.data.objects.new(name,data);scene.collection.objects.link(ob);ob.data.materials.append(material);return ob
def xyz(b,s,v):return (3.5*b,3.4*s,9*v)
verts=[xyz(b,s,D['sigma'][i][j]) for i,b in enumerate(D['b']) for j,s in enumerate(D['s'])]
ns=len(D['s']);nb=len(D['b']);faces=[]
for i in range(nb-1):
 for j in range(ns-1):
  a=i*ns+j;faces.append((a,a+ns,a+ns+1,a+1))
mesh=bpy.data.meshes.new('Evaluated fixed-b coefficient samples');mesh.from_pydata(verts,[],faces);mesh.update()
ob=bpy.data.objects.new('sigma = Psi_b(s)',mesh);scene.collection.objects.link(ob);ob.data.materials.append(blue)
for j in [0,ns-1]:
 curve('s='+str(D['s'][j]),[xyz(b,D['s'][j],D['sigma'][i][j]) for i,b in enumerate(D['b'])],dark if j==0 else orange,.017)
for j in range(0,ns,8):curve('surface cutoff grid',[xyz(b,D['s'][j],D['sigma'][i][j]) for i,b in enumerate(D['b'])],gray,.003)
for i in range(0,nb,8):curve('surface activation grid',[xyz(D['b'][i],s,D['sigma'][i][j]) for j,s in enumerate(D['s'])],gray,.003)
sigma=D['threshold_plane']
me=bpy.data.meshes.new('sigma plane');me.from_pydata([xyz(0,0,sigma),xyz(1,0,sigma),xyz(1,1,sigma),xyz(0,1,sigma)],[],[(0,1,2,3)]);me.update()
ob=bpy.data.objects.new('sigma = 0.075',me);scene.collection.objects.link(ob);ob.data.materials.append(plane)
pts=[]
for i,b in enumerate(D['b']):
 row=D['sigma'][i]
 if row[0]>=sigma>=row[-1]:
  for j in range(ns-1):
   if row[j]>=sigma>=row[j+1]:
    sf=D['s'][j]+(D['s'][j+1]-D['s'][j])*(row[j]-sigma)/(row[j]-row[j+1])
    pts.append(xyz(b,sf,sigma+.001));break
curve('Sampled threshold intersection',pts,yellow,.018)
for end in [(3.65,0,0),(0,3.55,0),(0,0,2.35)]:curve('coordinate axis',[(0,0,0),end],navy,.009)
for v in [0,.25,.5,.75,1]:
 curve('floor grid b',[(3.5*v,0,0),(3.5*v,3.4,0)],gray,.003)
 curve('floor grid s',[(0,3.4*v,0),(3.5,3.4*v,0)],gray,.003)
bpy.ops.object.camera_add(location=(7.3,-8.8,7.6));cam=bpy.context.object
target=Vector((1.65,1.5,.95));cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler()
cam.data.type='ORTHO';cam.data.ortho_scale=7.9;scene.camera=cam
fontpath=Path(r'C:\Windows\Fonts\segoeui.ttf');font=bpy.data.fonts.load(str(fontpath))
def txt(body,co,size=.12,material=navy):
 data=bpy.data.curves.new(body,'FONT');data.body=body;data.size=size;data.align_x='CENTER';data.font=font
 ob=bpy.data.objects.new(body,data);scene.collection.objects.link(ob);ob.location=co;ob.rotation_euler=cam.rotation_euler;data.materials.append(material);return ob
for v in [0,.25,.5,.75,1]:
 txt(str(v), (3.5*v,-.18,-.10),.13)
 if v:txt(str(v),(-.21,3.4*v,-.02),.13)
for v in [.05,.10,.15,.20]:
 curve('sigma tick',[(-.05,0,9*v),(.04,0,9*v)],navy,.005);txt(f'{v:.2f}',(-.26,-.03,9*v),.13)
txt('b: activation exponent',(1.9,-.6,-.08),.18)
txt('s: source degree',(-.6,2.9,.03),.18)
txt('sigma',(0,0,2.63),.19)
txt('s = 0',(3.88,-.06,2.30),.15,dark)
txt('s = 1',(3.66,3.4,9*D['sigma'][-1][-1]),.15,orange)
txt('sigma = 0.075',(3.85,2.15,9*sigma),.14,orange)
# Camera-oriented title and footer in a fixed screen plane.
rot=cam.rotation_euler.to_matrix();right=rot@Vector((1,0,0));up=rot@Vector((0,1,0))
center=target
def screen(body,x,y,size):
 return txt(body,center+right*x+up*y,size)
screen('ACTIVATION AND THE ORIGINAL HEAT THRESHOLD',0,2.58,.22)
screen('Surface: sigma = b psi((1 + s - b) / b)',0,2.28,.19)
screen('Above the plane: one full-source heat deficit. Below: zero.',0,-2.37,.155)
screen('Away from equality; limiting s = (N + 1 - q) / q.  A1, A20, A36-37; AP1-4.',0,-2.59,.115)
screen('Numerical surface of the proved coefficient. No xi zero or observed outlier is assigned.',0,-2.76,.115)
bpy.ops.object.light_add(type='AREA',location=(1,-3,8));bpy.context.object.data.energy=800;bpy.context.object.data.shape='DISK';bpy.context.object.data.size=8
bpy.ops.object.light_add(type='AREA',location=(-4,4,5));bpy.context.object.data.energy=500;bpy.context.object.data.size=6
scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(1,1,1,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=1
scene.render.filepath='//ACTIVATION_HEAT_THRESHOLD.png'
bpy.ops.wm.save_as_mainfile(filepath=str(O/'ACTIVATION_HEAT_THRESHOLD.blend'))
bpy.ops.render.render(write_still=True)
