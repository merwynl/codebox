import hou


def create_geo():
    obj = hou.node('/obj')
    geo_node = obj.createNode('geo', 'myGeo')
    box = geo_node.createNode('box', 'myCube')
    sphere = geo_node.createNode('sphere', 'mySphere')

    box.setInput(0,sphere,0)

    box.setDisplayFlag(1)
    box.setRenderFlag(1)
