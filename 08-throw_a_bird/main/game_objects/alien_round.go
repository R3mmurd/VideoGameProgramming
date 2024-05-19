components {
  id: "destructible"
  component: "/main/scripts/destructible.script"
  position {
    x: 0.0
    y: 0.0
    z: 0.0
  }
  rotation {
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0
  }
  properties {
    id: "energy"
    value: "400.0"
    type: PROPERTY_TYPE_NUMBER
  }
  properties {
    id: "undamaged"
    value: "alienGreen_round"
    type: PROPERTY_TYPE_HASH
  }
  properties {
    id: "damaged"
    value: "alienGreen_round"
    type: PROPERTY_TYPE_HASH
  }
  properties {
    id: "almost_destroyed"
    value: "alienGreen_round"
    type: PROPERTY_TYPE_HASH
  }
  properties {
    id: "debris"
    value: "false"
    type: PROPERTY_TYPE_BOOLEAN
  }
}
embedded_components {
  id: "sprite"
  type: "sprite"
  data: "default_animation: \"alienGreen_round\"\n"
  "material: \"/builtins/materials/sprite.material\"\n"
  "blend_mode: BLEND_MODE_ALPHA\n"
  "textures {\n"
  "  sampler: \"texture_sampler\"\n"
  "  texture: \"/main/atlas/characters.atlas\"\n"
  "}\n"
  ""
  position {
    x: 0.0
    y: 0.0
    z: 0.0
  }
  rotation {
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0
  }
}
embedded_components {
  id: "collisionobject"
  type: "collisionobject"
  data: "collision_shape: \"\"\n"
  "type: COLLISION_OBJECT_TYPE_DYNAMIC\n"
  "mass: 400.0\n"
  "friction: 0.9\n"
  "restitution: 0.1\n"
  "group: \"destructible\"\n"
  "mask: \"destructible\"\n"
  "mask: \"bird\"\n"
  "mask: \"ground\"\n"
  "mask: \"wind\"\n"
  "embedded_collision_shape {\n"
  "  shapes {\n"
  "    shape_type: TYPE_SPHERE\n"
  "    position {\n"
  "      x: 0.0\n"
  "      y: 0.0\n"
  "      z: 0.0\n"
  "    }\n"
  "    rotation {\n"
  "      x: 0.0\n"
  "      y: 0.0\n"
  "      z: 0.0\n"
  "      w: 1.0\n"
  "    }\n"
  "    index: 0\n"
  "    count: 1\n"
  "    id: \"\"\n"
  "  }\n"
  "  data: 35.0395\n"
  "}\n"
  "linear_damping: 0.1\n"
  "angular_damping: 0.7\n"
  "locked_rotation: false\n"
  "bullet: false\n"
  ""
  position {
    x: 0.0
    y: 0.0
    z: 0.0
  }
  rotation {
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0
  }
}
