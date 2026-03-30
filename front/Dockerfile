# Этап 1: Сборка
FROM node:20-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Этап 2: Продакшн (Nginx)
FROM nginx:stable-alpine as production-stage
# Копируем билд из первого этапа в папку, которую обслуживает nginx
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]