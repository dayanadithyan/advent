(ns solution.core
  (:require [clojure.string :as str])
  (:import [java.util ArrayList]))

(defn read-input [filename]
  (let [lines (slurp filename)
        inputs (str/split-lines lines)
        pairs []
        lists []
        prefixes (atom {})]
    (doseq [line inputs]
      (let [line (str/trim line)]
        (when-not (str/blank? line)
          (if (str/includes? line "|")
            (let [[a b] (str/split line #"\|")]
              (swap! prefixes update (Integer. b) (fnil conj []) (Integer. a)))
            (let [numbers (->> (str/split line #",")
                               (map str/trim)
                               (map #(Integer. %))
                               (filter identity))]
              (when-not (empty? numbers)
                (swap! lists conj numbers)))))))
    [lists @prefixes]))

(defn should-come-before [a b prefixes]
  (some #(= b %) (get prefixes a [])))

(defn custom-sort [lst prefixes]
  (let [result (ArrayList. lst)
        n (count lst)]
    (doseq [i (range n)]
      (doseq [j (range 0 (- n i 1))]
        (when (should-come-before (nth result (inc j)) (nth result j) prefixes)
          (let [temp (nth result j)]
            (.set result j (nth result (inc j)))
            (.set result (inc j) temp)))))
    (vec result)))

(defn middle [lst]
  (if (empty? lst) 0
      (nth lst (quot (count lst) 2))))

(defn solve [filename]
  (let [[lists prefixes] (read-input filename)
        part1 (atom 0)
        part2 (atom 0)]
    (doseq [lst lists]
      (when-not (empty? lst)
        (let [sorted-lst (atom nil)]
          (loop [i 0]
            (when (< i (count lst))
              (let [current (nth lst i)]
                (if (and (contains? prefixes current)
                         (some #(should-come-before current % prefixes) (subvec lst (inc i))))
                  (do
                    (reset! sorted-lst (custom-sort lst prefixes))
                    (swap! part2 + (middle @sorted-lst)))
                  (recur (inc i))))))
          (when-not @sorted-lst
            (swap! part1 + (middle lst))))))
    [@part1 @part2]))

(defn -main [& args]
  (try
    (let [[part1 part2] (solve "input.txt")]
      (println "Part 1:" part1)
      (println "Part 2:" part2))
    (catch Exception e
      (println "Error occurred:" (.getMessage e))
      (.printStackTrace e))))
