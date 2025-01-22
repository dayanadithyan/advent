(ns advent-of-code.y2024.day06
  (:require [clojure.set :as set]
            [clojure.string :as str]))

(def up 1i)
(def turn-right -1i)

(defn part-one [input]
  (let [[map-data start] (parse input)]
    (count (:positions (walk map-data start)))))

(defn part-two [input]
  (let [[map-data start] (parse input)]
    (count (filter
             (fn [pos]
               (:is-loop (walk (assoc map-data pos \#) start)))
             (:positions (walk map-data start))))))

(defn walk [map-data pos]
  (loop [seen #{}
         dir up
         pos pos]
    (if (or (not (map-data pos))
            (seen [pos dir]))
      {:positions (set (map first seen))
       :is-loop (seen [pos dir])}
      (recur
        (conj seen [pos dir])
        (if (= (map-data (+ pos dir)) \#)
          (* dir turn-right)
          dir)
        (if (= (map-data (+ pos dir)) \#)
          pos
          (+ pos dir))))))

(defn parse [input]
  (let [lines (str/split-lines input)
        map-data (reduce-kv
                   (fn [m y line]
                     (reduce-kv
                       (fn [m x char]
                         (assoc m (+ (- (* up y)) x) char))
                       m
                       (vec line)))
                   {}
                   (vec lines))
        start (first (filter #(= (val %) \^) map-data))]
    [map-data (key start)]))

(defn read-input []
  (slurp "input.txt"))

(defn -main []
  (let [input-data (read-input)]
    (println "Part One:" (part-one input-data))
    (println "Part Two:" (part-two input-data))))

(-main)
