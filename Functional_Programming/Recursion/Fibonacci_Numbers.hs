--Contributed by Ron Watkins
module Main where

fib :: Int -> Int
fib 1 = 0
fib 2 = 1
fib n = fib (n-1) + fib (n-2)
  
-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main :: IO ()
main = do
    input <- getLine
    print . fib . (read :: String -> Int) $ input