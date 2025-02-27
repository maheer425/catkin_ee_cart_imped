"""autogenerated by genpy from ee_cart_imped_msgs/EECartImpedActionResult.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ee_cart_imped_msgs.msg
import geometry_msgs.msg
import genpy
import actionlib_msgs.msg
import std_msgs.msg

class EECartImpedActionResult(genpy.Message):
  _md5sum = "084904f177cd8988e0a7f8680e1e8a21"
  _type = "ee_cart_imped_msgs/EECartImpedActionResult"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
EECartImpedResult result

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
MSG: actionlib_msgs/GoalStatus
GoalID goal_id
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server

#Allow for the user to associate a string with GoalStatus for debugging
string text


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
MSG: ee_cart_imped_msgs/EECartImpedResult
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#result definition
#whether it was successful
#the pose and force we ended with
Header header
bool success
ee_cart_imped_msgs/StiffPoint desired
geometry_msgs/Pose actual_pose
float64 effort_sq_error

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
  __slots__ = ['header','status','result']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalStatus','ee_cart_imped_msgs/EECartImpedResult']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,status,result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EECartImpedActionResult, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.result is None:
        self.result = ee_cart_imped_msgs.msg.EECartImpedResult()
    else:
      self.header = std_msgs.msg.Header()
      self.status = actionlib_msgs.msg.GoalStatus()
      self.result = ee_cart_imped_msgs.msg.EECartImpedResult()

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
      buff.write(_struct_2I.pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.status.status))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs))
      _x = self.result.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3I.pack(_x.result.success, _x.result.desired.header.seq, _x.result.desired.header.stamp.secs, _x.result.desired.header.stamp.nsecs))
      _x = self.result.desired.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d6B2i8d.pack(_x.result.desired.pose.position.x, _x.result.desired.pose.position.y, _x.result.desired.pose.position.z, _x.result.desired.pose.orientation.x, _x.result.desired.pose.orientation.y, _x.result.desired.pose.orientation.z, _x.result.desired.pose.orientation.w, _x.result.desired.wrench_or_stiffness.force.x, _x.result.desired.wrench_or_stiffness.force.y, _x.result.desired.wrench_or_stiffness.force.z, _x.result.desired.wrench_or_stiffness.torque.x, _x.result.desired.wrench_or_stiffness.torque.y, _x.result.desired.wrench_or_stiffness.torque.z, _x.result.desired.isForceX, _x.result.desired.isForceY, _x.result.desired.isForceZ, _x.result.desired.isTorqueX, _x.result.desired.isTorqueY, _x.result.desired.isTorqueZ, _x.result.desired.time_from_start.secs, _x.result.desired.time_from_start.nsecs, _x.result.actual_pose.position.x, _x.result.actual_pose.position.y, _x.result.actual_pose.position.z, _x.result.actual_pose.orientation.x, _x.result.actual_pose.orientation.y, _x.result.actual_pose.orientation.z, _x.result.actual_pose.orientation.w, _x.result.effort_sq_error))
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
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.result is None:
        self.result = ee_cart_imped_msgs.msg.EECartImpedResult()
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
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8')
      else:
        self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.result.success, _x.result.desired.header.seq, _x.result.desired.header.stamp.secs, _x.result.desired.header.stamp.nsecs,) = _struct_B3I.unpack(str[start:end])
      self.result.success = bool(self.result.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.desired.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.result.desired.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 182
      (_x.result.desired.pose.position.x, _x.result.desired.pose.position.y, _x.result.desired.pose.position.z, _x.result.desired.pose.orientation.x, _x.result.desired.pose.orientation.y, _x.result.desired.pose.orientation.z, _x.result.desired.pose.orientation.w, _x.result.desired.wrench_or_stiffness.force.x, _x.result.desired.wrench_or_stiffness.force.y, _x.result.desired.wrench_or_stiffness.force.z, _x.result.desired.wrench_or_stiffness.torque.x, _x.result.desired.wrench_or_stiffness.torque.y, _x.result.desired.wrench_or_stiffness.torque.z, _x.result.desired.isForceX, _x.result.desired.isForceY, _x.result.desired.isForceZ, _x.result.desired.isTorqueX, _x.result.desired.isTorqueY, _x.result.desired.isTorqueZ, _x.result.desired.time_from_start.secs, _x.result.desired.time_from_start.nsecs, _x.result.actual_pose.position.x, _x.result.actual_pose.position.y, _x.result.actual_pose.position.z, _x.result.actual_pose.orientation.x, _x.result.actual_pose.orientation.y, _x.result.actual_pose.orientation.z, _x.result.actual_pose.orientation.w, _x.result.effort_sq_error,) = _struct_13d6B2i8d.unpack(str[start:end])
      self.result.desired.isForceX = bool(self.result.desired.isForceX)
      self.result.desired.isForceY = bool(self.result.desired.isForceY)
      self.result.desired.isForceZ = bool(self.result.desired.isForceZ)
      self.result.desired.isTorqueX = bool(self.result.desired.isTorqueX)
      self.result.desired.isTorqueY = bool(self.result.desired.isTorqueY)
      self.result.desired.isTorqueZ = bool(self.result.desired.isTorqueZ)
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
      buff.write(_struct_2I.pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.status.status))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs))
      _x = self.result.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B3I.pack(_x.result.success, _x.result.desired.header.seq, _x.result.desired.header.stamp.secs, _x.result.desired.header.stamp.nsecs))
      _x = self.result.desired.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_13d6B2i8d.pack(_x.result.desired.pose.position.x, _x.result.desired.pose.position.y, _x.result.desired.pose.position.z, _x.result.desired.pose.orientation.x, _x.result.desired.pose.orientation.y, _x.result.desired.pose.orientation.z, _x.result.desired.pose.orientation.w, _x.result.desired.wrench_or_stiffness.force.x, _x.result.desired.wrench_or_stiffness.force.y, _x.result.desired.wrench_or_stiffness.force.z, _x.result.desired.wrench_or_stiffness.torque.x, _x.result.desired.wrench_or_stiffness.torque.y, _x.result.desired.wrench_or_stiffness.torque.z, _x.result.desired.isForceX, _x.result.desired.isForceY, _x.result.desired.isForceZ, _x.result.desired.isTorqueX, _x.result.desired.isTorqueY, _x.result.desired.isTorqueZ, _x.result.desired.time_from_start.secs, _x.result.desired.time_from_start.nsecs, _x.result.actual_pose.position.x, _x.result.actual_pose.position.y, _x.result.actual_pose.position.z, _x.result.actual_pose.orientation.x, _x.result.actual_pose.orientation.y, _x.result.actual_pose.orientation.z, _x.result.actual_pose.orientation.w, _x.result.effort_sq_error))
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
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.result is None:
        self.result = ee_cart_imped_msgs.msg.EECartImpedResult()
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
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8')
      else:
        self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.result.success, _x.result.desired.header.seq, _x.result.desired.header.stamp.secs, _x.result.desired.header.stamp.nsecs,) = _struct_B3I.unpack(str[start:end])
      self.result.success = bool(self.result.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.desired.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.result.desired.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 182
      (_x.result.desired.pose.position.x, _x.result.desired.pose.position.y, _x.result.desired.pose.position.z, _x.result.desired.pose.orientation.x, _x.result.desired.pose.orientation.y, _x.result.desired.pose.orientation.z, _x.result.desired.pose.orientation.w, _x.result.desired.wrench_or_stiffness.force.x, _x.result.desired.wrench_or_stiffness.force.y, _x.result.desired.wrench_or_stiffness.force.z, _x.result.desired.wrench_or_stiffness.torque.x, _x.result.desired.wrench_or_stiffness.torque.y, _x.result.desired.wrench_or_stiffness.torque.z, _x.result.desired.isForceX, _x.result.desired.isForceY, _x.result.desired.isForceZ, _x.result.desired.isTorqueX, _x.result.desired.isTorqueY, _x.result.desired.isTorqueZ, _x.result.desired.time_from_start.secs, _x.result.desired.time_from_start.nsecs, _x.result.actual_pose.position.x, _x.result.actual_pose.position.y, _x.result.actual_pose.position.z, _x.result.actual_pose.orientation.x, _x.result.actual_pose.orientation.y, _x.result.actual_pose.orientation.z, _x.result.actual_pose.orientation.w, _x.result.effort_sq_error,) = _struct_13d6B2i8d.unpack(str[start:end])
      self.result.desired.isForceX = bool(self.result.desired.isForceX)
      self.result.desired.isForceY = bool(self.result.desired.isForceY)
      self.result.desired.isForceZ = bool(self.result.desired.isForceZ)
      self.result.desired.isTorqueX = bool(self.result.desired.isTorqueX)
      self.result.desired.isTorqueY = bool(self.result.desired.isTorqueY)
      self.result.desired.isTorqueZ = bool(self.result.desired.isTorqueZ)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_2I = struct.Struct("<2I")
_struct_13d6B2i8d = struct.Struct("<13d6B2i8d")
_struct_B3I = struct.Struct("<B3I")
