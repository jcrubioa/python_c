#pragma comment(linker, "/export:calculate")

long long calculate(int n){
    int i;
    long long c = 0;
    for(i=0; i < n; i++){
        c += i;
    }
    return c;
}