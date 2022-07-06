
(cl:in-package :asdf)

(defsystem "pa1_scara-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MoveLastJoint" :depends-on ("_package_MoveLastJoint"))
    (:file "_package_MoveLastJoint" :depends-on ("_package"))
  ))