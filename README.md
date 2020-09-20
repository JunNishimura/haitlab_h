# Anime Recommend System
![anime_group_photo](https://user-images.githubusercontent.com/28744711/93694092-b0274b80-fb42-11ea-91fa-ac753aa9720f.jpg)

本プロジェクトは[HaitLab Primaryコース4期](https://hait-lab.com/)の最終プロジェクトです。

## Member
- [Jun Nishimura](https://github.com/JunNishimura)： プロジェクト統括、システム全般
- [Koki Osumi](https://github.com/sumiship): home画面のフロントエンド実装

## Theme
コロナ禍で自宅で一人過ごす時間を少しでも楽しいものにするべく、アニメのレコメンドシステムを作成した。

## Gallery
#### home画面
![home](https://user-images.githubusercontent.com/28744711/93694096-b4536900-fb42-11ea-8946-43363ad242da.png)

#### 検索画面 / レコメンド表示
![search](https://user-images.githubusercontent.com/28744711/93694097-b87f8680-fb42-11ea-8eda-c4970bc2b2cb.png)

#### ジャンル選択 / レコメンド表示
![genre-search](https://user-images.githubusercontent.com/28744711/93694094-b1f10f00-fb42-11ea-8f3e-40853853be72.png)
![genre-result](https://user-images.githubusercontent.com/28744711/93694093-b1f10f00-fb42-11ea-975a-6cde9463ea4d.png)

## system overview
- ユーザーからの入力として好きなアニメタイトルを受け取りアニメをレコメンドする。
- ユーザーが選択したアニメのジャンルよりアニメをレコメンドする。

## technology
- webアプリケーションのフレームワークにはdjangoを使用
- cosine similarityより、各アイテムの評価をもとに類似度を算出

## Feature
レコメンドエンジンを構築するうえでフィルターバブルに注目した。
評価の良い作品やコサイン類似度より算出した類似度の高い作品のみをレコメンドするのではなく、評価の低い作品や類似度の低いも同時にレコメンドすることで、フィルターバブルに対策を試みた。

## Next Steps
セレンディピティや多様性を考慮したレコメンドシステムの研究は盛んみたいなので、それらをリサーチしつつもアニメに特化したレコメンドの方法を模索したい。
