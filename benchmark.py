"""Compare both versions with timeit and inspect them with cProfile."""
import timeit, cProfile, pstats, io
from original import count_unique_items as original_count
from optimized import count_unique_items as optimized_count
DATA = [i % 1500 for i in range(12000)]
def profile_function(fn, label):
    profiler=cProfile.Profile(); profiler.enable(); result=fn(DATA); profiler.disable()
    stream=io.StringIO(); pstats.Stats(profiler,stream=stream).sort_stats("cumtime").print_stats(10)
    print(f"\n--- cProfile: {label} (result={result}) ---"); print(stream.getvalue())
def main():
    assert original_count(DATA)==optimized_count(DATA)==1500
    old=timeit.repeat(lambda: original_count(DATA),repeat=5,number=1)
    new=timeit.repeat(lambda: optimized_count(DATA),repeat=5,number=1)
    a=sum(old)/len(old); b=sum(new)/len(new)
    print("Input size:",len(DATA)); print("Expected unique values: 1500")
    print("Original runs (seconds):",[round(x,6) for x in old])
    print("Optimized runs (seconds):",[round(x,6) for x in new])
    print("Original average (seconds):",round(a,6))
    print("Optimized average (seconds):",round(b,6))
    print("Execution-time reduction (%):",round((1-b/a)*100,2))
    print("Speedup (x):",round(a/b,2))
    profile_function(original_count,"original"); profile_function(optimized_count,"optimized")
if __name__=="__main__": main()
