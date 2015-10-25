import Text.Printf (printf)

-- This function should return a list [area, volume].
solve :: Int -> Int -> [Int] -> [Int] -> [Double]
solve l r a b = [area, volume]
    where rangeVals = map ((*0.001) . fromIntegral) [1000*l..1000*r] --weird hack, had problems with generating a float interval
          expr :: Double -> Double
          expr x =  sum [ fromIntegral aa * x ** fromIntegral bb|(aa, bb) <- zip a b]
          area = 0.001 * sum [expr range | range <- rangeVals]
          volume = 0.001 * pi*sum [ expr range ** 2 | range <- rangeVals]

--Input/Output.
main :: IO ()
main = getContents >>= mapM_ (printf "%.1f\n"). (\[a, b, [l, r]] -> solve l r a b). map (map read. words). lines