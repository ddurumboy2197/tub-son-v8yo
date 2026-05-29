**Python**
```python
import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_prime(16) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True
    assert is_prime(20) == False

def test_is_prime_edge_cases():
    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_prime(16) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True
    assert is_prime(20) == False

def test_is_prime_invalid_input():
    with pytest.raises(TypeError):
        is_prime("a")
    with pytest.raises(TypeError):
        is_prime(1.5)
```

**JavaScript (Jest)**
```javascript
describe('isPrime', () => {
    it('should return true for prime numbers', () => {
        expect(isPrime(2)).toBe(true);
        expect(isPrime(3)).toBe(true);
        expect(isPrime(4)).toBe(false);
        expect(isPrime(5)).toBe(true);
        expect(isPrime(6)).toBe(false);
        expect(isPrime(7)).toBe(true);
        expect(isPrime(8)).toBe(false);
        expect(isPrime(9)).toBe(false);
        expect(isPrime(10)).toBe(false);
        expect(isPrime(11)).toBe(true);
        expect(isPrime(12)).toBe(false);
        expect(isPrime(13)).toBe(true);
        expect(isPrime(14)).toBe(false);
        expect(isPrime(15)).toBe(false);
        expect(isPrime(16)).toBe(false);
        expect(isPrime(17)).toBe(true);
        expect(isPrime(18)).toBe(false);
        expect(isPrime(19)).toBe(true);
        expect(isPrime(20)).toBe(false);
    });

    it('should return false for non-prime numbers', () => {
        expect(isPrime(-1)).toBe(false);
        expect(isPrime(0)).toBe(false);
        expect(isPrime(1)).toBe(false);
        expect(isPrime(4)).toBe(false);
        expect(isPrime(6)).toBe(false);
        expect(isPrime(8)).toBe(false);
        expect(isPrime(9)).toBe(false);
        expect(isPrime(10)).toBe(false);
        expect(isPrime(12)).toBe(false);
        expect(isPrime(14)).toBe(false);
        expect(isPrime(15)).toBe(false);
        expect(isPrime(16)).toBe(false);
        expect(isPrime(18)).toBe(false);
        expect(isPrime(20)).toBe(false);
    });

    it('should throw an error for invalid input', () => {
        expect(() => isPrime("a")).toThrowError();
        expect(() => isPrime(1.5)).toThrowError();
    });
});
```
