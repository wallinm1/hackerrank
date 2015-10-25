factorial :: Int -> Double
factorial 0 = 1.0
factorial n = fromIntegral (product [1..n])

solve :: Double -> Double
solve x = sum [(x^^ex)/factorial ex | ex <- [0..9]]

main :: IO ()
main = getContents >>= mapM_ ((print . solve) . (read :: String -> Double)) . tail . words