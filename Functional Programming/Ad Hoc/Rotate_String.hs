-- Enter your code here. Read input from STDIN. Print output to STDOUT
rotate :: String -> Int -> [String]
rotate [] _ = [] --case when pattern matching fails
rotate _ n
    | n <= 0 = [] --base case for recursion
rotate (x:xs) n = rot : rotate rot (n-1) --general case, prepend rotated string, perform recursion
    where rot = xs ++ [x]
main :: IO ()
main = do
    _ <- readLn :: IO Int --read the first integer
    contents <- getContents
    let strings = lines contents
    let proc = [rotate x (length x) | x <- strings]
    mapM_ putStrLn [unwords x | x <- proc]