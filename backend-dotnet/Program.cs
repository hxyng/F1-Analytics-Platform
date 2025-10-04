public class FastF1Service
{
    private readonly HttpClient _http;

    public FastF1Service(HttpClient http) => _http = http;

    public async Task<string> GetLapTimes(int year, string gp, string driver)
    {
        return await _http.GetStringAsync($"http://localhost:8000/lap-times/{year}/{gp}/{driver}");
    }
}