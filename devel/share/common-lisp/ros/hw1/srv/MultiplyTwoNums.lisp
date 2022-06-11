; Auto-generated. Do not edit!


(cl:in-package hw1-srv)


;//! \htmlinclude MultiplyTwoNums-request.msg.html

(cl:defclass <MultiplyTwoNums-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:float
    :initform 0.0)
   (b
    :reader b
    :initarg :b
    :type cl:float
    :initform 0.0))
)

(cl:defclass MultiplyTwoNums-request (<MultiplyTwoNums-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MultiplyTwoNums-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MultiplyTwoNums-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hw1-srv:<MultiplyTwoNums-request> is deprecated: use hw1-srv:MultiplyTwoNums-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <MultiplyTwoNums-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw1-srv:a-val is deprecated.  Use hw1-srv:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <MultiplyTwoNums-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw1-srv:b-val is deprecated.  Use hw1-srv:b instead.")
  (b m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MultiplyTwoNums-request>) ostream)
  "Serializes a message object of type '<MultiplyTwoNums-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'b))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MultiplyTwoNums-request>) istream)
  "Deserializes a message object of type '<MultiplyTwoNums-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'a) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'b) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MultiplyTwoNums-request>)))
  "Returns string type for a service object of type '<MultiplyTwoNums-request>"
  "hw1/MultiplyTwoNumsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MultiplyTwoNums-request)))
  "Returns string type for a service object of type 'MultiplyTwoNums-request"
  "hw1/MultiplyTwoNumsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MultiplyTwoNums-request>)))
  "Returns md5sum for a message object of type '<MultiplyTwoNums-request>"
  "fa76f5fbe76a971f9b1d5d312793b2e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MultiplyTwoNums-request)))
  "Returns md5sum for a message object of type 'MultiplyTwoNums-request"
  "fa76f5fbe76a971f9b1d5d312793b2e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MultiplyTwoNums-request>)))
  "Returns full string definition for message of type '<MultiplyTwoNums-request>"
  (cl:format cl:nil "float64 a~%float64 b~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MultiplyTwoNums-request)))
  "Returns full string definition for message of type 'MultiplyTwoNums-request"
  (cl:format cl:nil "float64 a~%float64 b~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MultiplyTwoNums-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MultiplyTwoNums-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MultiplyTwoNums-request
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
))
;//! \htmlinclude MultiplyTwoNums-response.msg.html

(cl:defclass <MultiplyTwoNums-response> (roslisp-msg-protocol:ros-message)
  ((product
    :reader product
    :initarg :product
    :type cl:float
    :initform 0.0))
)

(cl:defclass MultiplyTwoNums-response (<MultiplyTwoNums-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MultiplyTwoNums-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MultiplyTwoNums-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hw1-srv:<MultiplyTwoNums-response> is deprecated: use hw1-srv:MultiplyTwoNums-response instead.")))

(cl:ensure-generic-function 'product-val :lambda-list '(m))
(cl:defmethod product-val ((m <MultiplyTwoNums-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw1-srv:product-val is deprecated.  Use hw1-srv:product instead.")
  (product m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MultiplyTwoNums-response>) ostream)
  "Serializes a message object of type '<MultiplyTwoNums-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'product))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MultiplyTwoNums-response>) istream)
  "Deserializes a message object of type '<MultiplyTwoNums-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'product) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MultiplyTwoNums-response>)))
  "Returns string type for a service object of type '<MultiplyTwoNums-response>"
  "hw1/MultiplyTwoNumsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MultiplyTwoNums-response)))
  "Returns string type for a service object of type 'MultiplyTwoNums-response"
  "hw1/MultiplyTwoNumsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MultiplyTwoNums-response>)))
  "Returns md5sum for a message object of type '<MultiplyTwoNums-response>"
  "fa76f5fbe76a971f9b1d5d312793b2e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MultiplyTwoNums-response)))
  "Returns md5sum for a message object of type 'MultiplyTwoNums-response"
  "fa76f5fbe76a971f9b1d5d312793b2e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MultiplyTwoNums-response>)))
  "Returns full string definition for message of type '<MultiplyTwoNums-response>"
  (cl:format cl:nil "~%float64 product~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MultiplyTwoNums-response)))
  "Returns full string definition for message of type 'MultiplyTwoNums-response"
  (cl:format cl:nil "~%float64 product~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MultiplyTwoNums-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MultiplyTwoNums-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MultiplyTwoNums-response
    (cl:cons ':product (product msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MultiplyTwoNums)))
  'MultiplyTwoNums-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MultiplyTwoNums)))
  'MultiplyTwoNums-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MultiplyTwoNums)))
  "Returns string type for a service object of type '<MultiplyTwoNums>"
  "hw1/MultiplyTwoNums")