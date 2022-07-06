; Auto-generated. Do not edit!


(cl:in-package pa1_scara-srv)


;//! \htmlinclude MoveLastJoint-request.msg.html

(cl:defclass <MoveLastJoint-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0)
   (z
    :reader z
    :initarg :z
    :type cl:integer
    :initform 0))
)

(cl:defclass MoveLastJoint-request (<MoveLastJoint-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveLastJoint-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveLastJoint-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pa1_scara-srv:<MoveLastJoint-request> is deprecated: use pa1_scara-srv:MoveLastJoint-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <MoveLastJoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pa1_scara-srv:x-val is deprecated.  Use pa1_scara-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <MoveLastJoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pa1_scara-srv:y-val is deprecated.  Use pa1_scara-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <MoveLastJoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pa1_scara-srv:z-val is deprecated.  Use pa1_scara-srv:z instead.")
  (z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveLastJoint-request>) ostream)
  "Serializes a message object of type '<MoveLastJoint-request>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'z)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveLastJoint-request>) istream)
  "Deserializes a message object of type '<MoveLastJoint-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'z) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveLastJoint-request>)))
  "Returns string type for a service object of type '<MoveLastJoint-request>"
  "pa1_scara/MoveLastJointRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveLastJoint-request)))
  "Returns string type for a service object of type 'MoveLastJoint-request"
  "pa1_scara/MoveLastJointRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveLastJoint-request>)))
  "Returns md5sum for a message object of type '<MoveLastJoint-request>"
  "95da2541c9d6989c0876f480a9b1c7e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveLastJoint-request)))
  "Returns md5sum for a message object of type 'MoveLastJoint-request"
  "95da2541c9d6989c0876f480a9b1c7e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveLastJoint-request>)))
  "Returns full string definition for message of type '<MoveLastJoint-request>"
  (cl:format cl:nil "int64 x~%int64 y~%int64 z~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveLastJoint-request)))
  "Returns full string definition for message of type 'MoveLastJoint-request"
  (cl:format cl:nil "int64 x~%int64 y~%int64 z~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveLastJoint-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveLastJoint-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveLastJoint-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
))
;//! \htmlinclude MoveLastJoint-response.msg.html

(cl:defclass <MoveLastJoint-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass MoveLastJoint-response (<MoveLastJoint-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveLastJoint-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveLastJoint-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pa1_scara-srv:<MoveLastJoint-response> is deprecated: use pa1_scara-srv:MoveLastJoint-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveLastJoint-response>) ostream)
  "Serializes a message object of type '<MoveLastJoint-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveLastJoint-response>) istream)
  "Deserializes a message object of type '<MoveLastJoint-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveLastJoint-response>)))
  "Returns string type for a service object of type '<MoveLastJoint-response>"
  "pa1_scara/MoveLastJointResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveLastJoint-response)))
  "Returns string type for a service object of type 'MoveLastJoint-response"
  "pa1_scara/MoveLastJointResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveLastJoint-response>)))
  "Returns md5sum for a message object of type '<MoveLastJoint-response>"
  "95da2541c9d6989c0876f480a9b1c7e4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveLastJoint-response)))
  "Returns md5sum for a message object of type 'MoveLastJoint-response"
  "95da2541c9d6989c0876f480a9b1c7e4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveLastJoint-response>)))
  "Returns full string definition for message of type '<MoveLastJoint-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveLastJoint-response)))
  "Returns full string definition for message of type 'MoveLastJoint-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveLastJoint-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveLastJoint-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveLastJoint-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MoveLastJoint)))
  'MoveLastJoint-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MoveLastJoint)))
  'MoveLastJoint-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveLastJoint)))
  "Returns string type for a service object of type '<MoveLastJoint>"
  "pa1_scara/MoveLastJoint")