
(cl:in-package :asdf)

(defsystem "pa1-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "HT" :depends-on ("_package_HT"))
    (:file "_package_HT" :depends-on ("_package"))
  ))