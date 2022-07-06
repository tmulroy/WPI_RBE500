
(cl:in-package :asdf)

(defsystem "pa1-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "joint_variables" :depends-on ("_package_joint_variables"))
    (:file "_package_joint_variables" :depends-on ("_package"))
  ))