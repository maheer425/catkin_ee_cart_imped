"""autogenerated by genpy from ee_cart_imped_msgs/EECartImpedActionGoal.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ee_cart_imped_msgs.msg
import geometry_msgs.msg
import genpy
import actionlib_msgs.msg
import std_msgs.msg

class EECartImpedActionGoal(genpy.Message):
  _md5sum = "09251e687b897c24590030b27467eb9f"
  _type = "ee_cart_imped_msgs/EECartImpedActionGoal"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
EECartImpedGoal goal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: ee_cart_imped_msgs/EECartImpedGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#goal definition
Header header
ee_cart_imped_msgs/StiffPoint[] trajectory

================================================================================
MSG: ee_cart_imped_msgs/StiffPoint
Header header
#The pose to achieve in the stiffness directions
geometry_msgs/Pose pose
#Wrench or stiffness for each dimension
geometry_msgs/Wrench wrench_or_stiffness
#The following are True if a force/torque should
#be exerted and False if a stiffness should be used.
bool isForceX
bool isForceY
bool isForceZ
bool isTorqueX
bool isTorqueY
bool isTorqueZ
#The time from the start of the trajectory that this
#point should be achieved.
duration time_from_start
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Wrench
# This represents force in free space, seperated into 
# it's linear and angular parts.  
Vector3  force
Vector3  torque

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
"""
  __slots__ = ['header','goal_id','goal']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalID','ee_cart_imped_msgs/EECartImpedGoal']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,goal_id,goal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EECartImpedActionGoal, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = ee_cart_imped_msgs.msg.EECartImpedGoal()
    else:
      self.header = std_msgs.msg.Header()
      self.goal_id = actionlib_msgs.msg.GoalID()
      self.goal = ee_cart_imped_msgs.msg.EECartImpedGoal()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs))
      _x = self.goal.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.goal.trajectory)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory:
        _v1 = val1.header
        buff.write(_struct_I.pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v3 = val1.pose
        _v4 = _v3.position
        _x = _v4
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v5 = _v3.orientation
        _x = _v5
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v6 = val1.wrench_or_stiffness
        _v7 = _v6.force
        _x = _v7
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v8 = _v6.torque
        _x = _v8
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_6B.pack(_x.isForceX, _x.isForceY, _x.isForceZ, _x.isTorqueX, _x.isTorqueY, _x.isTorqueZ))
        _v9 = val1.time_from_start
        _x = _v9
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = ee_cart_imped_msgs.msg.EECartImpedGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory = []
      for i in range(0, length):
        val1 = ee_cart_imped_msgs.msg.StiffPoint()
        _v10 = val1.header
        start = end
        end += 4
        (_v10.seq,) = _struct_I.unpack(str[start:end])
        _v11 = _v10.stamp
        _x = _v11
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v10.frame_id = str[start:end].decode('utf-8')
        else:
          _v10.frame_id = str[start:end]
        _v12 = val1.pose
        _v13 = _v12.position
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v14 = _v12.orientation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _v15 = val1.wrench_or_stiffness
        _v16 = _v15.force
        _x = _v16
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v17 = _v15.torque
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 6
        (_x.isForceX, _x.isForceY, _x.isForceZ, _x.isTorqueX, _x.isTorqueY, _x.isTorqueZ,) = _struct_6B.unpack(str[start:end])
        val1.isForceX = bool(val1.isForceX)
        val1.isForceY = bool(val1.isForceY)
        val1.isForceZ = bool(val1.isForceZ)
        val1.isTorqueX = bool(val1.isTorqueX)
        val1.isTorqueY = bool(val1.isTorqueY)
        val1.isTorqueZ = bool(val1.isTorqueZ)
        _v18 = val1.time_from_start
        _x = _v18
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.goal.trajectory.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs))
      _x = self.goal.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.goal.trajectory)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory:
        _v19 = val1.header
        buff.write(_struct_I.pack(_v19.seq))
        _v20 = _v19.stamp
        _x = _v20
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v19.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v21 = val1.pose
        _v22 = _v21.position
        _x = _v22
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v23 = _v21.orientation
        _x = _v23
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v24 = val1.wrench_or_stiffness
        _v25 = _v24.force
        _x = _v25
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v26 = _v24.torque
        _x = _v26
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_6B.pack(_x.isForceX, _x.isForceY, _x.isForceZ, _x.isTorqueX, _x.isTorqueY, _x.isTorqueZ))
        _v27 = val1.time_from_start
        _x = _v27
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = ee_cart_imped_msgs.msg.EECartImpedGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory = []
      for i in range(0, length):
        val1 = ee_cart_imped_msgs.msg.StiffPoint()
        _v28 = val1.header
        start = end
        end += 4
        (_v28.seq,) = _struct_I.unpack(str[start:end])
        _v29 = _v28.stamp
        _x = _v29
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v28.frame_id = str[start:end].decode('utf-8')
        else:
          _v28.frame_id = str[start:end]
        _v30 = val1.pose
        _v31 = _v30.position
        _x = _v31
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v32 = _v30.orientation
        _x = _v32
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _v33 = val1.wrench_or_stiffness
        _v34 = _v33.force
        _x = _v34
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v35 = _v33.torque
        _x = _v35
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 6
        (_x.isForceX, _x.isForceY, _x.isForceZ, _x.isTorqueX, _x.isTorqueY, _x.isTorqueZ,) = _struct_6B.unpack(str[start:end])
        val1.isForceX = bool(val1.isForceX)
        val1.isForceY = bool(val1.isForceY)
        val1.isForceZ = bool(val1.isForceZ)
        val1.isTorqueX = bool(val1.isTorqueX)
        val1.isTorqueY = bool(val1.isTorqueY)
        val1.isTorqueZ = bool(val1.isTorqueZ)
        _v36 = val1.time_from_start
        _x = _v36
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.goal.trajectory.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6B = struct.Struct("<6B")
_struct_2i = struct.Struct("<2i")
_struct_3I = struct.Struct("<3I")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
