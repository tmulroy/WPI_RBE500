
(cl:in-package :asdf)

(defsystem "fk-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "JointVariables" :depends-on ("_package_JointVariables"))
    (:file "_package_JointVariables" :depends-on ("_package"))
  ))