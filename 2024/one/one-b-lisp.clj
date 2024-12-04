(ql:quickload :alexandria)

(defun read-file (filename)
  (uiop:read-file-string filename))

(defun parse-input (input-str)
  (let ((lines (uiop:split-string input-str :separator '(#\Newline))))
    (loop for line in lines
          for (left right) = (mapcar #'parse-integer (uiop:split-string line))
          collect left into lefts
          collect right into rights
          finally (return (values lefts rights)))))

(defun calculate-list-distance (left-list right-list)
  (let ((sorted-left (sort (copy-list left-list) #'<))
        (sorted-right (sort (copy-list right-list) #'<)))
    (loop for left in sorted-left
          for right in sorted-right
          summing (abs (- left right)))))

(let* ((input-str (read-file "/Volumes/LNX/NEW/advent/advent/2024/one/input.txt"))
       (left-list right-list) (parse-input input-str))
  (format t "Total distance: ~a~%" (calculate-list-distance left-list right-list)))