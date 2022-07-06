
(cl:in-package :asdf)

(defsystem "pa1_scara-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ReferencePosition" :depends-on ("_package_ReferencePosition"))
    (:file "_package_ReferencePosition" :depends-on ("_package"))
  ))