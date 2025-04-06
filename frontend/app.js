function submitForm() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const userData = { name, email, password };
    console.log("Yuborilayotgan ma'lumotlar:", userData);

    fetch('http://127.0.0.1:8000/user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server xatosi: ${response.status} - ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Serverdan kelgan javob:', data);
        alert('Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi!');
        document.getElementById('registerForm').reset();
    })
    .catch(error => {
        console.error('Xato:', error.message);
        alert('Xatolik yuz berdi, qayta urinib ko‘ring.');
    });
}