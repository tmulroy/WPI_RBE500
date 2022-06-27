;; Auto-generated. Do not edit!


(when (boundp 'fk::JointVariables)
  (if (not (find-package "FK"))
    (make-package "FK"))
  (shadow 'JointVariables (find-package "FK")))
(unless (find-package "FK::JOINTVARIABLES")
  (make-package "FK::JOINTVARIABLES"))

(in-package "ROS")
;;//! \htmlinclude JointVariables.msg.html


(defclass fk::JointVariables
  :super ros::object
  :slots (_q1 _q2 _q3 _q4 _q5 _q6 ))

(defmethod fk::JointVariables
  (:init
   (&key
    ((:q1 __q1) 0.0)
    ((:q2 __q2) 0.0)
    ((:q3 __q3) 0.0)
    ((:q4 __q4) 0.0)
    ((:q5 __q5) 0.0)
    ((:q6 __q6) 0.0)
    )
   (send-super :init)
   (setq _q1 (float __q1))
   (setq _q2 (float __q2))
   (setq _q3 (float __q3))
   (setq _q4 (float __q4))
   (setq _q5 (float __q5))
   (setq _q6 (float __q6))
   self)
  (:q1
   (&optional __q1)
   (if __q1 (setq _q1 __q1)) _q1)
  (:q2
   (&optional __q2)
   (if __q2 (setq _q2 __q2)) _q2)
  (:q3
   (&optional __q3)
   (if __q3 (setq _q3 __q3)) _q3)
  (:q4
   (&optional __q4)
   (if __q4 (setq _q4 __q4)) _q4)
  (:q5
   (&optional __q5)
   (if __q5 (setq _q5 __q5)) _q5)
  (:q6
   (&optional __q6)
   (if __q6 (setq _q6 __q6)) _q6)
  (:serialization-length
   ()
   (+
    ;; float64 _q1
    8
    ;; float64 _q2
    8
    ;; float64 _q3
    8
    ;; float64 _q4
    8
    ;; float64 _q5
    8
    ;; float64 _q6
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
     ;; float64 _q3
       (sys::poke _q3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _q4
       (sys::poke _q4 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _q5
       (sys::poke _q5 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _q6
       (sys::poke _q6 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _q1
     (setq _q1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _q2
     (setq _q2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _q3
     (setq _q3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _q4
     (setq _q4 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _q5
     (setq _q5 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _q6
     (setq _q6 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get fk::JointVariables :md5sum-) "a61a219e6f5b1a7fbfc4c6ce5b5c4482")
(setf (get fk::JointVariables :datatype-) "fk/JointVariables")
(setf (get fk::JointVariables :definition-)
      "float64 q1
float64 q2
float64 q3
float64 q4
float64 q5
float64 q6

")



(provide :fk/JointVariables "a61a219e6f5b1a7fbfc4c6ce5b5c4482")


