;; Auto-generated. Do not edit!


(when (boundp 'hw1::Num)
  (if (not (find-package "HW1"))
    (make-package "HW1"))
  (shadow 'Num (find-package "HW1")))
(unless (find-package "HW1::NUM")
  (make-package "HW1::NUM"))

(in-package "ROS")
;;//! \htmlinclude Num.msg.html


(defclass hw1::Num
  :super ros::object
  :slots (_num ))

(defmethod hw1::Num
  (:init
   (&key
    ((:num __num) 0.0)
    )
   (send-super :init)
   (setq _num (float __num))
   self)
  (:num
   (&optional __num)
   (if __num (setq _num __num)) _num)
  (:serialization-length
   ()
   (+
    ;; float64 _num
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _num
       (sys::poke _num (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _num
     (setq _num (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get hw1::Num :md5sum-) "f942a3e0cbd340847b2a0e5b31a783fe")
(setf (get hw1::Num :datatype-) "hw1/Num")
(setf (get hw1::Num :definition-)
      "float64 num

")



(provide :hw1/Num "f942a3e0cbd340847b2a0e5b31a783fe")


