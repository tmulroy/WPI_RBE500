;; Auto-generated. Do not edit!


(when (boundp 'pa1::HT)
  (if (not (find-package "PA1"))
    (make-package "PA1"))
  (shadow 'HT (find-package "PA1")))
(unless (find-package "PA1::HT")
  (make-package "PA1::HT"))
(unless (find-package "PA1::HTREQUEST")
  (make-package "PA1::HTREQUEST"))
(unless (find-package "PA1::HTRESPONSE")
  (make-package "PA1::HTRESPONSE"))

(in-package "ROS")





(defclass pa1::HTRequest
  :super ros::object
  :slots (_ht11 _ht12 _ht13 _ht14 _ht21 _ht22 _ht23 _ht24 _ht31 _ht32 _ht33 _ht34 _ht41 _ht42 _ht43 _ht44 ))

(defmethod pa1::HTRequest
  (:init
   (&key
    ((:ht11 __ht11) 0.0)
    ((:ht12 __ht12) 0.0)
    ((:ht13 __ht13) 0.0)
    ((:ht14 __ht14) 0.0)
    ((:ht21 __ht21) 0.0)
    ((:ht22 __ht22) 0.0)
    ((:ht23 __ht23) 0.0)
    ((:ht24 __ht24) 0.0)
    ((:ht31 __ht31) 0.0)
    ((:ht32 __ht32) 0.0)
    ((:ht33 __ht33) 0.0)
    ((:ht34 __ht34) 0.0)
    ((:ht41 __ht41) 0.0)
    ((:ht42 __ht42) 0.0)
    ((:ht43 __ht43) 0.0)
    ((:ht44 __ht44) 0.0)
    )
   (send-super :init)
   (setq _ht11 (float __ht11))
   (setq _ht12 (float __ht12))
   (setq _ht13 (float __ht13))
   (setq _ht14 (float __ht14))
   (setq _ht21 (float __ht21))
   (setq _ht22 (float __ht22))
   (setq _ht23 (float __ht23))
   (setq _ht24 (float __ht24))
   (setq _ht31 (float __ht31))
   (setq _ht32 (float __ht32))
   (setq _ht33 (float __ht33))
   (setq _ht34 (float __ht34))
   (setq _ht41 (float __ht41))
   (setq _ht42 (float __ht42))
   (setq _ht43 (float __ht43))
   (setq _ht44 (float __ht44))
   self)
  (:ht11
   (&optional __ht11)
   (if __ht11 (setq _ht11 __ht11)) _ht11)
  (:ht12
   (&optional __ht12)
   (if __ht12 (setq _ht12 __ht12)) _ht12)
  (:ht13
   (&optional __ht13)
   (if __ht13 (setq _ht13 __ht13)) _ht13)
  (:ht14
   (&optional __ht14)
   (if __ht14 (setq _ht14 __ht14)) _ht14)
  (:ht21
   (&optional __ht21)
   (if __ht21 (setq _ht21 __ht21)) _ht21)
  (:ht22
   (&optional __ht22)
   (if __ht22 (setq _ht22 __ht22)) _ht22)
  (:ht23
   (&optional __ht23)
   (if __ht23 (setq _ht23 __ht23)) _ht23)
  (:ht24
   (&optional __ht24)
   (if __ht24 (setq _ht24 __ht24)) _ht24)
  (:ht31
   (&optional __ht31)
   (if __ht31 (setq _ht31 __ht31)) _ht31)
  (:ht32
   (&optional __ht32)
   (if __ht32 (setq _ht32 __ht32)) _ht32)
  (:ht33
   (&optional __ht33)
   (if __ht33 (setq _ht33 __ht33)) _ht33)
  (:ht34
   (&optional __ht34)
   (if __ht34 (setq _ht34 __ht34)) _ht34)
  (:ht41
   (&optional __ht41)
   (if __ht41 (setq _ht41 __ht41)) _ht41)
  (:ht42
   (&optional __ht42)
   (if __ht42 (setq _ht42 __ht42)) _ht42)
  (:ht43
   (&optional __ht43)
   (if __ht43 (setq _ht43 __ht43)) _ht43)
  (:ht44
   (&optional __ht44)
   (if __ht44 (setq _ht44 __ht44)) _ht44)
  (:serialization-length
   ()
   (+
    ;; float64 _ht11
    8
    ;; float64 _ht12
    8
    ;; float64 _ht13
    8
    ;; float64 _ht14
    8
    ;; float64 _ht21
    8
    ;; float64 _ht22
    8
    ;; float64 _ht23
    8
    ;; float64 _ht24
    8
    ;; float64 _ht31
    8
    ;; float64 _ht32
    8
    ;; float64 _ht33
    8
    ;; float64 _ht34
    8
    ;; float64 _ht41
    8
    ;; float64 _ht42
    8
    ;; float64 _ht43
    8
    ;; float64 _ht44
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _ht11
       (sys::poke _ht11 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht12
       (sys::poke _ht12 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht13
       (sys::poke _ht13 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht14
       (sys::poke _ht14 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht21
       (sys::poke _ht21 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht22
       (sys::poke _ht22 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht23
       (sys::poke _ht23 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht24
       (sys::poke _ht24 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht31
       (sys::poke _ht31 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht32
       (sys::poke _ht32 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht33
       (sys::poke _ht33 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht34
       (sys::poke _ht34 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht41
       (sys::poke _ht41 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht42
       (sys::poke _ht42 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht43
       (sys::poke _ht43 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ht44
       (sys::poke _ht44 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _ht11
     (setq _ht11 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht12
     (setq _ht12 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht13
     (setq _ht13 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht14
     (setq _ht14 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht21
     (setq _ht21 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht22
     (setq _ht22 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht23
     (setq _ht23 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht24
     (setq _ht24 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht31
     (setq _ht31 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht32
     (setq _ht32 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht33
     (setq _ht33 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht34
     (setq _ht34 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht41
     (setq _ht41 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht42
     (setq _ht42 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht43
     (setq _ht43 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ht44
     (setq _ht44 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass pa1::HTResponse
  :super ros::object
  :slots (_q1 _q2 _d3 ))

(defmethod pa1::HTResponse
  (:init
   (&key
    ((:q1 __q1) 0.0)
    ((:q2 __q2) 0.0)
    ((:d3 __d3) 0.0)
    )
   (send-super :init)
   (setq _q1 (float __q1))
   (setq _q2 (float __q2))
   (setq _d3 (float __d3))
   self)
  (:q1
   (&optional __q1)
   (if __q1 (setq _q1 __q1)) _q1)
  (:q2
   (&optional __q2)
   (if __q2 (setq _q2 __q2)) _q2)
  (:d3
   (&optional __d3)
   (if __d3 (setq _d3 __d3)) _d3)
  (:serialization-length
   ()
   (+
    ;; float64 _q1
    8
    ;; float64 _q2
    8
    ;; float64 _d3
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _q1
       (sys::poke _q1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _q2
       (sys::poke _q2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _d3
       (sys::poke _d3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _q1
     (setq _q1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _q2
     (setq _q2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _d3
     (setq _d3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass pa1::HT
  :super ros::object
  :slots ())

(setf (get pa1::HT :md5sum-) "41bf0543de79fcb6f767b6c9848b88ec")
(setf (get pa1::HT :datatype-) "pa1/HT")
(setf (get pa1::HT :request) pa1::HTRequest)
(setf (get pa1::HT :response) pa1::HTResponse)

(defmethod pa1::HTRequest
  (:response () (instance pa1::HTResponse :init)))

(setf (get pa1::HTRequest :md5sum-) "41bf0543de79fcb6f767b6c9848b88ec")
(setf (get pa1::HTRequest :datatype-) "pa1/HTRequest")
(setf (get pa1::HTRequest :definition-)
      "float64 ht11
float64 ht12
float64 ht13
float64 ht14
float64 ht21
float64 ht22
float64 ht23
float64 ht24
float64 ht31
float64 ht32
float64 ht33
float64 ht34
float64 ht41
float64 ht42
float64 ht43
float64 ht44
---
float64 q1
float64 q2
float64 d3


")

(setf (get pa1::HTResponse :md5sum-) "41bf0543de79fcb6f767b6c9848b88ec")
(setf (get pa1::HTResponse :datatype-) "pa1/HTResponse")
(setf (get pa1::HTResponse :definition-)
      "float64 ht11
float64 ht12
float64 ht13
float64 ht14
float64 ht21
float64 ht22
float64 ht23
float64 ht24
float64 ht31
float64 ht32
float64 ht33
float64 ht34
float64 ht41
float64 ht42
float64 ht43
float64 ht44
---
float64 q1
float64 q2
float64 d3


")



(provide :pa1/HT "41bf0543de79fcb6f767b6c9848b88ec")


