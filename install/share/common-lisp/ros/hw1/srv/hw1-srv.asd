
(cl:in-package :asdf)

(defsystem "hw1-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MultiplyTwoNums" :depends-on ("_package_MultiplyTwoNums"))
    (:file "_package_MultiplyTwoNums" :depends-on ("_package"))
  ))