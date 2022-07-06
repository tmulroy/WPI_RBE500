;; Auto-generated. Do not edit!


(when (boundp 'pa1::joint_variables)
  (if (not (find-package "PA1"))
    (make-package "PA1"))
  (shadow 'joint_variables (find-package "PA1")))
(unless (find-package "PA1::JOINT_VARIABLES")
  (make-package "PA1::JOINT_VARIABLES"))

(in-package "ROS")
;;//! \htmlinclude joint_variables.msg.html


(defclass pa1::joint_variables
  :super ros::object
  :slots (_q1 _q2 _d3 ))

(defmethod pa1::joint_variables
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

(setf (get pa1::joint_variables :md5sum-) "f439218c3a6a6da84daea3b1bccc8aa6")
(setf (get pa1::joint_variables :datatype-) "pa1/joint_variables")
(setf (get pa1::joint_variables :definition-)
      "float64 q1
float64 q2
float64 d3
")



(provide :pa1/joint_variables "f439218c3a6a6da84daea3b1bccc8aa6")


