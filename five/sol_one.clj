
(ns solution
  (:require [clojure.java.io :as io]
            [clojure.string :as str]))

;; Read and process input file
(def input
  (slurp "input.txt"))

(def inputs
  (str/split input #"\n\n"))

(def pairs
  (->> (first inputs)
       (str/split-lines)
       (map #(mapv #(Integer/parseInt %) (str/split % #"\|")))))

(def lists
  (->> (second inputs)
       (str/split-lines)
       (map #(mapv #(Integer/parseInt %) (str/split % #",")))))

;; Group pairs by their second value
(def prefixes
  (->> pairs
       (group-by second)
       (into {} (map (fn [[k v]] [k (map first v)])))))

;; Custom comparator function
(defn compare [x y]
  (if (some #(= y %) (get prefixes x []))
    -1
    1))

;; Function to get the middle element of a list
(defn middle [lst]
  (nth lst (quot (count lst) 2)))

;; Calculate part1 and part2
(defn calculate []
  (let [results (reduce
                  (fn [acc lst]
                    (loop [i 0]
                      (if (< i (count lst))
                        (if-let [things (get prefixes (nth lst i))]
                          (if (some #(contains? (set things) %) (drop (inc i) lst))
                            (do
                              (let [sorted-list (sort compare lst)]
                                (update acc :part2 + (middle sorted-list)))
                              (recur (count lst)))
                            (recur (inc i)))
                          (recur (inc i)))
                        (update acc :part1 + (middle lst)))))
                  {:part1 0 :part2 0}
                  lists)]
    results))

;; Execute calculation and print results
(let [{:keys [part1 part2]} (calculate)]
  (println (str "Part 1: " part1))
  (println (str "Part 2: " part2)))


