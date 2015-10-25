f :: Integral a => [a] -> a
f arr = sum [odds | odds <- arr, odd odds]-- Fill up this function body

main :: IO ()
main = do
   inputdata <- getContents
   print (f $ map (read :: String -> Int) $ lines inputdata)