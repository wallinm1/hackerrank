fact :: Int -> Double
fact n
    | n <= 0 = 1.0
    | otherwise = fromIntegral (product [1..n])
pascalRow :: Int -> Int -> [String]
pascalRow n r
    | n < 0 = []
    | r < 0 = []
    | otherwise = show (round x :: Int) : pascalRow n (r - 1)
        where x = fact n/(fact r * fact (n - r))
main :: IO ()     
main = do
    n <- readLn :: IO Int --read the first integer
    let rows = [pascalRow x x | x <- [0..(n-1)]]
    mapM_ putStrLn [unwords x | x <- rows]