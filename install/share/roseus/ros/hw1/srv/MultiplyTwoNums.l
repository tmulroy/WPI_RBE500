;; Auto-generated. Do not edit!


(when (boundp 'hw1::MultiplyTwoNums)
  (if (not (find-package "HW1"))
    (make-package "HW1"))
  (shadow 'MultiplyTwoNums (find-package "HW1")))
(unless (find-package "HW1::MULTIPLYTWONUMS")
  (make-package "HW1::MULTIPLYTWONUMS"))
(unless (find-package "HW1::MULTIPLYTWONUMSREQUEST")
  (make-package "HW1::MULTIPLYTWONUMSREQUEST"))
(unless (find-package "HW1::MULTIPLYTWONUMSRESPONSE")
  (make-package "HW1::MULTIPLYTWONUMSRESPONSE"))

(in-package "ROS")





(defclass hw1::MultiplyTwoNumsRequest
  :super ros::object
  :slots (_a _b ))

(defmethod hw1::MultiplyTwoNumsRequest
  (:init
   (&key
    ((:a __a) 0.0)
    ((:b __b) 0.0)
    )
   (send-super :init)
   (setq _a (float __a))
   (setq _b (float __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; float64 _a
    8
    ;; float64 _b
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _a
       (sys::poke _a (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _b
       (sys::poke _b (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _a
     (setq _a (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _b
     (setq _b (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass hw1::MultiplyTwoNumsResponse
  :super ros::object
  :slots (_product ))

(defmethod hw1::MultiplyTwoNumsResponse
  (:init
   (&key
    ((:product __product) 0.0)
    )
   (send-super :init)
   (setq _product (float __product))
   self)
  (:product
   (&optional __product)
   (if __product (setq _product __product)) _product)
  (:serialization-length
   ()
   (+
    ;; float64 _product
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _product
       (sys::poke _product (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _product
     (setq _product (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass hw1::MultiplyTwoNums
  :super ros::object
  :slots ())

(setf (get hw1::MultiplyTwoNums :md5sum-) "fa76f5fbe76a971f9b1d5d312793b2e8")
(setf (get hw1::MultiplyTwoNums :datatype-) "hw1/MultiplyTwoNums")
(setf (get hw1::MultiplyTwoNums :request) hw1::MultiplyTwoNumsRequest)
(setf (get hw1::MultiplyTwoNums :response) hw1::MultiplyTwoNumsResponse)

(defmethod hw1::MultiplyTwoNumsRequest
  (:response () (instance hw1::MultiplyTwoNumsResponse :init)))

(setf (get hw1::MultiplyTwoNumsRequest :md5sum-) "fa76f5fbe76a971f9b1d5d312793b2e8")
(setf (get hw1::MultiplyTwoNumsRequest :datatype-) "hw1/MultiplyTwoNumsRequest")
(setf (get hw1::MultiplyTwoNumsRequest :definition-)
      "float64 a
float64 b

---

float64 product

")

(setf (get hw1::MultiplyTwoNumsResponse :md5sum-) "fa76f5fbe76a971f9b1d5d312793b2e8")
(setf (get hw1::MultiplyTwoNumsResponse :datatype-) "hw1/MultiplyTwoNumsResponse")
(setf (get hw1::MultiplyTwoNumsResponse :definition-)
      "float64 a
float64 b

---

float64 product

")



(provide :hw1/MultiplyTwoNums "fa76f5fbe76a971f9b1d5d312793b2e8")


