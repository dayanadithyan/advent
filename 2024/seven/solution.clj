(ns advent-of-code.y2024.day07
  (:require [clojure.string :as str]))

(defn parse-line [line]
  (let [nums (map #(Long/parseLong %) (re-seq #"\d+" line))]
    {:target (first nums)
     :nums (rest nums)}))

(defn parse-input [input]
  (map parse-line (str/split-lines input)))

(defn check1 [target acc nums]
  (cond
    (empty? nums) (= target acc)
    :else (or (check1 target (* acc (first nums)) (rest nums))
              (check1 target (+ acc (first nums)) (rest nums)))))

(defn check2 [target acc nums]
  (cond
    (> acc target) false
    (empty? nums) (= target acc)
    :else (or (check2 target (Long/parseLong (str acc (first nums))) (rest nums))
              (check2 target (* acc (first nums)) (rest nums))
              (check2 target (+ acc (first nums)) (rest nums)))))

(defn filter-valid [input checker]
  (->> (parse-input input)
       (filter (fn [{:keys [target nums]}]
                 (checker target (first nums) (rest nums))))
       (map :target)))

(defn part-one [input]
  (reduce + (filter-valid input check1)))

(defn part-two [input]
  (reduce + (filter-valid input check2)))

(defn read-input []
  (slurp "input.txt"))

(defn -main []
  (let [input-data (read-input)]
    (println "Part One:" (part-one input-data))
    (println "Part Two:" (part-two input-data))))

(-main)
