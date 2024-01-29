%Convert USD to other currencies%

usd = input('Enter amount (US Dollars): ');
fprintf('Amount in USD: %1.2f\n',usd)

eur = usd * 0.93;
fprintf('Amount in Euros: %1.2f\n',eur)

krw = usd * 1334.40;
fprintf('Amount in South Korean Won: %1.2f\n',krw)

rub = usd * 89;
fprintf('Amount in Russian Rubles: %1.2f\n', rub)

aud = usd * 1.52;
fprintf('Amount in Australian Dollars: %1.2f\n', aud)

php = usd * 56.36;
fprintf('Amount in Philippine Pesos: %1.2f\n', php)