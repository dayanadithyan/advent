    (ns list-processor.core
  (:require [clojure.string :as str]
            [clojure.java.io :as io]))

(defn parse-input [input-str]
  (let [lines (str/split-lines (str/trim input-str))
        parsed (map #(map read-string (str/split % #"\s+")) lines)]
    (apply map vector parsed)))

(defn calculate-list-distance [left-list right-list]
  (->> (map vector (sort left-list) (sort right-list))
       (map #(Math/abs (- (first %) (second %))))
       (reduce +)))

(defn read-input-file [file-path]
  (slurp file-path))

(defn process-first-part []
  (let [input-str (read-input-file "/Volumes/LNX/NEW/advent/advent/2024/one/input.txt")
        [left-list right-list] (parse-input input-str)]
    (println "Total distance:" (calculate-list-distance left-list right-list))))

(defn process-second-part []
  (let [lines (line-seq (io/reader "input2.txt"))
        parsed (map #(map read-string (str/split (str/trim %) #"\s+")) lines)
        [left right] (apply map vector parsed)
        right-counts (frequencies right)
        similarity-score (reduce + (map #(* % (get right-counts %)) left))]
    (println similarity-score)))

(defn -main []
  (process-first-part)
  (process-second-part))