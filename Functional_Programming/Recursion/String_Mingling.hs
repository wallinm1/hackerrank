-- Enter your code here. Read input from STDIN. Print output to STDOUT
main :: IO ()
main = do
    p <- getLine
    q <- getLine
    putStrLn (concat [x : [y]| (x, y) <- zip p q])