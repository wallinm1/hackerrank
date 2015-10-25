f :: [Int] -> [Int]
f lst = case lst of
    _:y:lst2 -> y : f lst2 --case where list has two elements or more, remove first element and recurse
    _ -> [] -- case where list has one element or less.

-- This part deals with the Input and Output and can be used as it is. Do not modify it.
main :: IO ()
main = do
   inputdata <- getContents
   mapM_ print. f. map read. lines $ inputdata