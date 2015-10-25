-- Enter your code here. Read input from STDIN. Print output to STDOUT
f :: [Int] -> [Int]
f [] = []
f [x] = [abs x]
f (x:xs) = abs x : f xs

-- This section handles the Input/Output and can be used as it is. Do not modify it.
main :: IO ()
main = do
   inputdata <- getContents
   mapM_ print (f $ map (read :: String -> Int) $ lines inputdata)