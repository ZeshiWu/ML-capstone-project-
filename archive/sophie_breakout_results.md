# PPO agent
```
A.L.E: Arcade Learning Environment (version 0.8.1+53f58b7)
[Powered by Stella]
Using cpu device
Wrapping the env with a `Monitor` wrapper
Wrapping the env in a DummyVecEnv.
Wrapping the env in a VecTransposeImage.
---------------------------------
| rollout/           |          |
|    ep_len_mean     | 202      |
|    ep_rew_mean     | 1.8      |
| time/              |          |
|    fps             | 180      |
|    iterations      | 1        |
|    time_elapsed    | 11       |
|    total_timesteps | 2048     |
---------------------------------
------------------------------------------
| rollout/                |              |
|    ep_len_mean          | 192          |
|    ep_rew_mean          | 1.48         |
| time/                   |              |
|    fps                  | 74           |
|    iterations           | 2            |
|    time_elapsed         | 55           |
|    total_timesteps      | 4096         |
| train/                  |              |
|    approx_kl            | 0.0142255565 |
|    clip_fraction        | 0.0624       |
|    clip_range           | 0.2          |
|    entropy_loss         | -1.38        |
|    explained_variance   | -0.0204      |
|    learning_rate        | 0.0003       |
|    loss                 | -0.0199      |
|    n_updates            | 10           |
|    policy_gradient_loss | -0.0113      |
|    value_loss           | 0.049        |
------------------------------------------
-----------------------------------------
| rollout/                |             |
|    ep_len_mean          | 198         |
|    ep_rew_mean          | 1.67        |
| time/                   |             |
|    fps                  | 62          |
|    iterations           | 3           |
|    time_elapsed         | 97          |
|    total_timesteps      | 6144        |
| train/                  |             |
|    approx_kl            | 0.039744124 |
|    clip_fraction        | 0.322       |
|    clip_range           | 0.2         |
|    entropy_loss         | -1.35       |
|    explained_variance   | 0.646       |
|    learning_rate        | 0.0003      |
|    loss                 | -0.0789     |
|    n_updates            | 20          |
|    policy_gradient_loss | -0.059      |
|    value_loss           | 0.0114      |
-----------------------------------------
-----------------------------------------
| rollout/                |             |
|    ep_len_mean          | 205         |
|    ep_rew_mean          | 1.87        |
| time/                   |             |
|    fps                  | 58          |
|    iterations           | 4           |
|    time_elapsed         | 139         |
|    total_timesteps      | 8192        |
| train/                  |             |
|    approx_kl            | 0.050227404 |
|    clip_fraction        | 0.428       |
|    clip_range           | 0.2         |
|    entropy_loss         | -1.3        |
|    explained_variance   | 0.651       |
|    learning_rate        | 0.0003      |
|    loss                 | -0.102      |
|    n_updates            | 30          |
|    policy_gradient_loss | -0.0774     |
|    value_loss           | 0.0149      |
-----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 215        |
|    ep_rew_mean          | 2.09       |
| time/                   |            |
|    fps                  | 57         |
|    iterations           | 5          |
|    time_elapsed         | 178        |
|    total_timesteps      | 10240      |
| train/                  |            |
|    approx_kl            | 0.07465796 |
|    clip_fraction        | 0.51       |
|    clip_range           | 0.2        |
|    entropy_loss         | -1.23      |
|    explained_variance   | 0.598      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.118     |
|    n_updates            | 40         |
|    policy_gradient_loss | -0.0883    |
|    value_loss           | 0.0162     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 220        |
|    ep_rew_mean          | 2.24       |
| time/                   |            |
|    fps                  | 56         |
|    iterations           | 6          |
|    time_elapsed         | 218        |
|    total_timesteps      | 12288      |
| train/                  |            |
|    approx_kl            | 0.08600013 |
|    clip_fraction        | 0.53       |
|    clip_range           | 0.2        |
|    entropy_loss         | -1.21      |
|    explained_variance   | 0.649      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.116     |
|    n_updates            | 50         |
|    policy_gradient_loss | -0.09      |
|    value_loss           | 0.0151     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 222        |
|    ep_rew_mean          | 2.33       |
| time/                   |            |
|    fps                  | 56         |
|    iterations           | 7          |
|    time_elapsed         | 252        |
|    total_timesteps      | 14336      |
| train/                  |            |
|    approx_kl            | 0.09992318 |
|    clip_fraction        | 0.555      |
|    clip_range           | 0.2        |
|    entropy_loss         | -1.14      |
|    explained_variance   | 0.731      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.117     |
|    n_updates            | 60         |
|    policy_gradient_loss | -0.0956    |
|    value_loss           | 0.0113     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 231        |
|    ep_rew_mean          | 2.57       |
| time/                   |            |
|    fps                  | 56         |
|    iterations           | 8          |
|    time_elapsed         | 291        |
|    total_timesteps      | 16384      |
| train/                  |            |
|    approx_kl            | 0.12376116 |
|    clip_fraction        | 0.589      |
|    clip_range           | 0.2        |
|    entropy_loss         | -1.08      |
|    explained_variance   | 0.767      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.126     |
|    n_updates            | 70         |
|    policy_gradient_loss | -0.1       |
|    value_loss           | 0.0116     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 233        |
|    ep_rew_mean          | 2.66       |
| time/                   |            |
|    fps                  | 55         |
|    iterations           | 9          |
|    time_elapsed         | 333        |
|    total_timesteps      | 18432      |
| train/                  |            |
|    approx_kl            | 0.14572254 |
|    clip_fraction        | 0.61       |
|    clip_range           | 0.2        |
|    entropy_loss         | -1.07      |
|    explained_variance   | 0.716      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.147     |
|    n_updates            | 80         |
|    policy_gradient_loss | -0.105     |
|    value_loss           | 0.0119     |
----------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 238       |
|    ep_rew_mean          | 2.81      |
| time/                   |           |
|    fps                  | 54        |
|    iterations           | 10        |
|    time_elapsed         | 374       |
|    total_timesteps      | 20480     |
| train/                  |           |
|    approx_kl            | 0.1840753 |
|    clip_fraction        | 0.629     |
|    clip_range           | 0.2       |
|    entropy_loss         | -1.01     |
|    explained_variance   | 0.728     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.104    |
|    n_updates            | 90        |
|    policy_gradient_loss | -0.105    |
|    value_loss           | 0.0115    |
---------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 245        |
|    ep_rew_mean          | 3.05       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 11         |
|    time_elapsed         | 415        |
|    total_timesteps      | 22528      |
| train/                  |            |
|    approx_kl            | 0.18073085 |
|    clip_fraction        | 0.598      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.932     |
|    explained_variance   | 0.788      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.132     |
|    n_updates            | 100        |
|    policy_gradient_loss | -0.0987    |
|    value_loss           | 0.0112     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 247        |
|    ep_rew_mean          | 3.12       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 12         |
|    time_elapsed         | 454        |
|    total_timesteps      | 24576      |
| train/                  |            |
|    approx_kl            | 0.22432551 |
|    clip_fraction        | 0.604      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.922     |
|    explained_variance   | 0.515      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.098     |
|    n_updates            | 110        |
|    policy_gradient_loss | -0.0907    |
|    value_loss           | 0.0206     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 254        |
|    ep_rew_mean          | 3.34       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 13         |
|    time_elapsed         | 492        |
|    total_timesteps      | 26624      |
| train/                  |            |
|    approx_kl            | 0.27002534 |
|    clip_fraction        | 0.639      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.865     |
|    explained_variance   | 0.73       |
|    learning_rate        | 0.0003     |
|    loss                 | -0.133     |
|    n_updates            | 120        |
|    policy_gradient_loss | -0.107     |
|    value_loss           | 0.0128     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 261        |
|    ep_rew_mean          | 3.63       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 14         |
|    time_elapsed         | 529        |
|    total_timesteps      | 28672      |
| train/                  |            |
|    approx_kl            | 0.23445758 |
|    clip_fraction        | 0.585      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.777     |
|    explained_variance   | 0.825      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.115     |
|    n_updates            | 130        |
|    policy_gradient_loss | -0.097     |
|    value_loss           | 0.0107     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 270        |
|    ep_rew_mean          | 3.87       |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 15         |
|    time_elapsed         | 568        |
|    total_timesteps      | 30720      |
| train/                  |            |
|    approx_kl            | 0.25249857 |
|    clip_fraction        | 0.583      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.798     |
|    explained_variance   | 0.716      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0787    |
|    n_updates            | 140        |
|    policy_gradient_loss | -0.0889    |
|    value_loss           | 0.0152     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 279        |
|    ep_rew_mean          | 4.16       |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 16         |
|    time_elapsed         | 607        |
|    total_timesteps      | 32768      |
| train/                  |            |
|    approx_kl            | 0.32808912 |
|    clip_fraction        | 0.593      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.764     |
|    explained_variance   | 0.742      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.128     |
|    n_updates            | 150        |
|    policy_gradient_loss | -0.0997    |
|    value_loss           | 0.0135     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 286        |
|    ep_rew_mean          | 4.39       |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 17         |
|    time_elapsed         | 645        |
|    total_timesteps      | 34816      |
| train/                  |            |
|    approx_kl            | 0.31781375 |
|    clip_fraction        | 0.563      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.738     |
|    explained_variance   | 0.818      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.107     |
|    n_updates            | 160        |
|    policy_gradient_loss | -0.0904    |
|    value_loss           | 0.01       |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 291        |
|    ep_rew_mean          | 4.53       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 18         |
|    time_elapsed         | 682        |
|    total_timesteps      | 36864      |
| train/                  |            |
|    approx_kl            | 0.31118208 |
|    clip_fraction        | 0.504      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.638     |
|    explained_variance   | 0.844      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.11      |
|    n_updates            | 170        |
|    policy_gradient_loss | -0.0841    |
|    value_loss           | 0.0108     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 298        |
|    ep_rew_mean          | 4.78       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 19         |
|    time_elapsed         | 717        |
|    total_timesteps      | 38912      |
| train/                  |            |
|    approx_kl            | 0.39606458 |
|    clip_fraction        | 0.535      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.623     |
|    explained_variance   | 0.838      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.112     |
|    n_updates            | 180        |
|    policy_gradient_loss | -0.089     |
|    value_loss           | 0.0118     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 304        |
|    ep_rew_mean          | 4.98       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 20         |
|    time_elapsed         | 756        |
|    total_timesteps      | 40960      |
| train/                  |            |
|    approx_kl            | 0.35669786 |
|    clip_fraction        | 0.503      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.579     |
|    explained_variance   | 0.656      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0984    |
|    n_updates            | 190        |
|    policy_gradient_loss | -0.076     |
|    value_loss           | 0.02       |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 309        |
|    ep_rew_mean          | 5.17       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 21         |
|    time_elapsed         | 794        |
|    total_timesteps      | 43008      |
| train/                  |            |
|    approx_kl            | 0.38966244 |
|    clip_fraction        | 0.514      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.586     |
|    explained_variance   | 0.814      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.123     |
|    n_updates            | 200        |
|    policy_gradient_loss | -0.0831    |
|    value_loss           | 0.0138     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 312        |
|    ep_rew_mean          | 5.3        |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 22         |
|    time_elapsed         | 833        |
|    total_timesteps      | 45056      |
| train/                  |            |
|    approx_kl            | 0.40389436 |
|    clip_fraction        | 0.514      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.605     |
|    explained_variance   | 0.664      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.102     |
|    n_updates            | 210        |
|    policy_gradient_loss | -0.0789    |
|    value_loss           | 0.0159     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 317        |
|    ep_rew_mean          | 5.47       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 23         |
|    time_elapsed         | 871        |
|    total_timesteps      | 47104      |
| train/                  |            |
|    approx_kl            | 0.39484224 |
|    clip_fraction        | 0.519      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.604     |
|    explained_variance   | 0.593      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0987    |
|    n_updates            | 220        |
|    policy_gradient_loss | -0.0729    |
|    value_loss           | 0.0203     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 319        |
|    ep_rew_mean          | 5.6        |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 24         |
|    time_elapsed         | 907        |
|    total_timesteps      | 49152      |
| train/                  |            |
|    approx_kl            | 0.43390125 |
|    clip_fraction        | 0.525      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.589     |
|    explained_variance   | 0.827      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.119     |
|    n_updates            | 230        |
|    policy_gradient_loss | -0.0871    |
|    value_loss           | 0.0104     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 324        |
|    ep_rew_mean          | 5.78       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 25         |
|    time_elapsed         | 947        |
|    total_timesteps      | 51200      |
| train/                  |            |
|    approx_kl            | 0.34159148 |
|    clip_fraction        | 0.512      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.599     |
|    explained_variance   | 0.694      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0988    |
|    n_updates            | 240        |
|    policy_gradient_loss | -0.0728    |
|    value_loss           | 0.022      |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 326        |
|    ep_rew_mean          | 5.86       |
| time/                   |            |
|    fps                  | 54         |
|    iterations           | 26         |
|    time_elapsed         | 983        |
|    total_timesteps      | 53248      |
| train/                  |            |
|    approx_kl            | 0.34867063 |
|    clip_fraction        | 0.542      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.614     |
|    explained_variance   | 0.563      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.109     |
|    n_updates            | 250        |
|    policy_gradient_loss | -0.0767    |
|    value_loss           | 0.0213     |
----------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 325       |
|    ep_rew_mean          | 5.87      |
| time/                   |           |
|    fps                  | 54        |
|    iterations           | 27        |
|    time_elapsed         | 1023      |
|    total_timesteps      | 55296     |
| train/                  |           |
|    approx_kl            | 0.3586975 |
|    clip_fraction        | 0.543     |
|    clip_range           | 0.2       |
|    entropy_loss         | -0.616    |
|    explained_variance   | 0.833     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.115    |
|    n_updates            | 260       |
|    policy_gradient_loss | -0.0895   |
|    value_loss           | 0.0113    |
---------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 331        |
|    ep_rew_mean          | 6.03       |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 28         |
|    time_elapsed         | 1065       |
|    total_timesteps      | 57344      |
| train/                  |            |
|    approx_kl            | 0.32653436 |
|    clip_fraction        | 0.529      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.634     |
|    explained_variance   | 0.732      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.118     |
|    n_updates            | 270        |
|    policy_gradient_loss | -0.0742    |
|    value_loss           | 0.0129     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 338        |
|    ep_rew_mean          | 6.19       |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 29         |
|    time_elapsed         | 1109       |
|    total_timesteps      | 59392      |
| train/                  |            |
|    approx_kl            | 0.40713876 |
|    clip_fraction        | 0.572      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.641     |
|    explained_variance   | 0.744      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.138     |
|    n_updates            | 280        |
|    policy_gradient_loss | -0.0948    |
|    value_loss           | 0.0132     |
----------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 340       |
|    ep_rew_mean          | 6.27      |
| time/                   |           |
|    fps                  | 53        |
|    iterations           | 30        |
|    time_elapsed         | 1153      |
|    total_timesteps      | 61440     |
| train/                  |           |
|    approx_kl            | 0.3988409 |
|    clip_fraction        | 0.557     |
|    clip_range           | 0.2       |
|    entropy_loss         | -0.641    |
|    explained_variance   | 0.727     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.0956   |
|    n_updates            | 290       |
|    policy_gradient_loss | -0.0899   |
|    value_loss           | 0.0141    |
---------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 340        |
|    ep_rew_mean          | 6.2        |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 31         |
|    time_elapsed         | 1195       |
|    total_timesteps      | 63488      |
| train/                  |            |
|    approx_kl            | 0.43886864 |
|    clip_fraction        | 0.53       |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.584     |
|    explained_variance   | 0.758      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0821    |
|    n_updates            | 300        |
|    policy_gradient_loss | -0.0808    |
|    value_loss           | 0.0178     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 340        |
|    ep_rew_mean          | 6.25       |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 32         |
|    time_elapsed         | 1234       |
|    total_timesteps      | 65536      |
| train/                  |            |
|    approx_kl            | 0.38976395 |
|    clip_fraction        | 0.54       |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.601     |
|    explained_variance   | 0.775      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.103     |
|    n_updates            | 310        |
|    policy_gradient_loss | -0.0863    |
|    value_loss           | 0.015      |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 344        |
|    ep_rew_mean          | 6.39       |
| time/                   |            |
|    fps                  | 53         |
|    iterations           | 33         |
|    time_elapsed         | 1271       |
|    total_timesteps      | 67584      |
| train/                  |            |
|    approx_kl            | 0.51348746 |
|    clip_fraction        | 0.554      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.623     |
|    explained_variance   | 0.614      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.121     |
|    n_updates            | 320        |
|    policy_gradient_loss | -0.0761    |
|    value_loss           | 0.0173     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 348        |
|    ep_rew_mean          | 6.56       |
| time/                   |            |
|    fps                  | 52         |
|    iterations           | 34         |
|    time_elapsed         | 1321       |
|    total_timesteps      | 69632      |
| train/                  |            |
|    approx_kl            | 0.32617435 |
|    clip_fraction        | 0.51       |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.593     |
|    explained_variance   | 0.757      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0647    |
|    n_updates            | 330        |
|    policy_gradient_loss | -0.0738    |
|    value_loss           | 0.0129     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 347        |
|    ep_rew_mean          | 6.68       |
| time/                   |            |
|    fps                  | 52         |
|    iterations           | 35         |
|    time_elapsed         | 1366       |
|    total_timesteps      | 71680      |
| train/                  |            |
|    approx_kl            | 0.32007217 |
|    clip_fraction        | 0.52       |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.604     |
|    explained_variance   | 0.657      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0983    |
|    n_updates            | 340        |
|    policy_gradient_loss | -0.0696    |
|    value_loss           | 0.0218     |
----------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 345       |
|    ep_rew_mean          | 6.69      |
| time/                   |           |
|    fps                  | 52        |
|    iterations           | 36        |
|    time_elapsed         | 1408      |
|    total_timesteps      | 73728     |
| train/                  |           |
|    approx_kl            | 0.3548572 |
|    clip_fraction        | 0.508     |
|    clip_range           | 0.2       |
|    entropy_loss         | -0.607    |
|    explained_variance   | 0.592     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.111    |
|    n_updates            | 350       |
|    policy_gradient_loss | -0.0661   |
|    value_loss           | 0.0236    |
---------------------------------------
--------------------------------------
| rollout/                |          |
|    ep_len_mean          | 346      |
|    ep_rew_mean          | 6.73     |
| time/                   |          |
|    fps                  | 52       |
|    iterations           | 37       |
|    time_elapsed         | 1455     |
|    total_timesteps      | 75776    |
| train/                  |          |
|    approx_kl            | 0.31881  |
|    clip_fraction        | 0.496    |
|    clip_range           | 0.2      |
|    entropy_loss         | -0.651   |
|    explained_variance   | 0.817    |
|    learning_rate        | 0.0003   |
|    loss                 | -0.101   |
|    n_updates            | 360      |
|    policy_gradient_loss | -0.0687  |
|    value_loss           | 0.0166   |
--------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 342        |
|    ep_rew_mean          | 6.64       |
| time/                   |            |
|    fps                  | 51         |
|    iterations           | 38         |
|    time_elapsed         | 1497       |
|    total_timesteps      | 77824      |
| train/                  |            |
|    approx_kl            | 0.33102018 |
|    clip_fraction        | 0.518      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.609     |
|    explained_variance   | 0.814      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0602    |
|    n_updates            | 370        |
|    policy_gradient_loss | -0.0801    |
|    value_loss           | 0.0127     |
----------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 342       |
|    ep_rew_mean          | 6.69      |
| time/                   |           |
|    fps                  | 51        |
|    iterations           | 39        |
|    time_elapsed         | 1537      |
|    total_timesteps      | 79872     |
| train/                  |           |
|    approx_kl            | 0.2776803 |
|    clip_fraction        | 0.479     |
|    clip_range           | 0.2       |
|    entropy_loss         | -0.635    |
|    explained_variance   | 0.794     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.0892   |
|    n_updates            | 380       |
|    policy_gradient_loss | -0.0693   |
|    value_loss           | 0.0235    |
---------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 342        |
|    ep_rew_mean          | 6.74       |
| time/                   |            |
|    fps                  | 51         |
|    iterations           | 40         |
|    time_elapsed         | 1580       |
|    total_timesteps      | 81920      |
| train/                  |            |
|    approx_kl            | 0.22917332 |
|    clip_fraction        | 0.47       |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.636     |
|    explained_variance   | 0.854      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0915    |
|    n_updates            | 390        |
|    policy_gradient_loss | -0.0653    |
|    value_loss           | 0.0143     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 344        |
|    ep_rew_mean          | 6.83       |
| time/                   |            |
|    fps                  | 51         |
|    iterations           | 41         |
|    time_elapsed         | 1621       |
|    total_timesteps      | 83968      |
| train/                  |            |
|    approx_kl            | 0.26106653 |
|    clip_fraction        | 0.486      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.657     |
|    explained_variance   | 0.592      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0789    |
|    n_updates            | 400        |
|    policy_gradient_loss | -0.0709    |
|    value_loss           | 0.0206     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 343        |
|    ep_rew_mean          | 6.81       |
| time/                   |            |
|    fps                  | 51         |
|    iterations           | 42         |
|    time_elapsed         | 1665       |
|    total_timesteps      | 86016      |
| train/                  |            |
|    approx_kl            | 0.23446432 |
|    clip_fraction        | 0.525      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.696     |
|    explained_variance   | 0.862      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0938    |
|    n_updates            | 410        |
|    policy_gradient_loss | -0.0742    |
|    value_loss           | 0.0156     |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 343        |
|    ep_rew_mean          | 6.91       |
| time/                   |            |
|    fps                  | 51         |
|    iterations           | 43         |
|    time_elapsed         | 1715       |
|    total_timesteps      | 88064      |
| train/                  |            |
|    approx_kl            | 0.29638547 |
|    clip_fraction        | 0.562      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.717     |
|    explained_variance   | 0.5        |
|    learning_rate        | 0.0003     |
|    loss                 | -0.0849    |
|    n_updates            | 420        |
|    policy_gradient_loss | -0.0857    |
|    value_loss           | 0.0242     |
----------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 341       |
|    ep_rew_mean          | 6.85      |
| time/                   |           |
|    fps                  | 51        |
|    iterations           | 44        |
|    time_elapsed         | 1756      |
|    total_timesteps      | 90112     |
| train/                  |           |
|    approx_kl            | 0.3029929 |
|    clip_fraction        | 0.554     |
|    clip_range           | 0.2       |
|    entropy_loss         | -0.72     |
|    explained_variance   | 0.672     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.103    |
|    n_updates            | 430       |
|    policy_gradient_loss | -0.0788   |
|    value_loss           | 0.019     |
---------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 334       |
|    ep_rew_mean          | 6.66      |
| time/                   |           |
|    fps                  | 51        |
|    iterations           | 45        |
|    time_elapsed         | 1799      |
|    total_timesteps      | 92160     |
| train/                  |           |
|    approx_kl            | 0.2561829 |
|    clip_fraction        | 0.59      |
|    clip_range           | 0.2       |
|    entropy_loss         | -0.768    |
|    explained_variance   | 0.796     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.115    |
|    n_updates            | 440       |
|    policy_gradient_loss | -0.0953   |
|    value_loss           | 0.0149    |
---------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 334        |
|    ep_rew_mean          | 6.71       |
| time/                   |            |
|    fps                  | 50         |
|    iterations           | 46         |
|    time_elapsed         | 1847       |
|    total_timesteps      | 94208      |
| train/                  |            |
|    approx_kl            | 0.30243683 |
|    clip_fraction        | 0.599      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.733     |
|    explained_variance   | 0.844      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.13      |
|    n_updates            | 450        |
|    policy_gradient_loss | -0.102     |
|    value_loss           | 0.0103     |
----------------------------------------
---------------------------------------
| rollout/                |           |
|    ep_len_mean          | 337       |
|    ep_rew_mean          | 6.85      |
| time/                   |           |
|    fps                  | 50        |
|    iterations           | 47        |
|    time_elapsed         | 1888      |
|    total_timesteps      | 96256     |
| train/                  |           |
|    approx_kl            | 0.3133288 |
|    clip_fraction        | 0.507     |
|    clip_range           | 0.2       |
|    entropy_loss         | -0.66     |
|    explained_variance   | 0.735     |
|    learning_rate        | 0.0003    |
|    loss                 | -0.127    |
|    n_updates            | 460       |
|    policy_gradient_loss | -0.0701   |
|    value_loss           | 0.0165    |
---------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 335        |
|    ep_rew_mean          | 6.8        |
| time/                   |            |
|    fps                  | 50         |
|    iterations           | 48         |
|    time_elapsed         | 1931       |
|    total_timesteps      | 98304      |
| train/                  |            |
|    approx_kl            | 0.30627716 |
|    clip_fraction        | 0.545      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.664     |
|    explained_variance   | 0.914      |
|    learning_rate        | 0.0003     |
|    loss                 | -0.136     |
|    n_updates            | 470        |
|    policy_gradient_loss | -0.0911    |
|    value_loss           | 0.00839    |
----------------------------------------
----------------------------------------
| rollout/                |            |
|    ep_len_mean          | 340        |
|    ep_rew_mean          | 6.93       |
| time/                   |            |
|    fps                  | 50         |
|    iterations           | 49         |
|    time_elapsed         | 1972       |
|    total_timesteps      | 100352     |
| train/                  |            |
|    approx_kl            | 0.35802665 |
|    clip_fraction        | 0.521      |
|    clip_range           | 0.2        |
|    entropy_loss         | -0.594     |
|    explained_variance   | 0.78       |
|    learning_rate        | 0.0003     |
|    loss                 | -0.104     |
|    n_updates            | 480        |
|    policy_gradient_loss | -0.0853    |
|    value_loss           | 0.014      |
----------------------------------------
```

# DQN agent
```
A.L.E: Arcade Learning Environment (version 0.8.1+53f58b7)
[Powered by Stella]
Using cpu device
Wrapping the env with a `Monitor` wrapper
Wrapping the env in a DummyVecEnv.
Wrapping the env in a VecTransposeImage.
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 208      |
|    ep_rew_mean      | 2        |
|    exploration_rate | 0.921    |
| time/               |          |
|    episodes         | 4        |
|    fps              | 17       |
|    time_elapsed     | 48       |
|    total_timesteps  | 831      |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 4.2e-05  |
|    n_updates        | 182      |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 187      |
|    ep_rew_mean      | 1.38     |
|    exploration_rate | 0.858    |
| time/               |          |
|    episodes         | 8        |
|    fps              | 12       |
|    time_elapsed     | 122      |
|    total_timesteps  | 1498     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.0153   |
|    n_updates        | 349      |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 192      |
|    ep_rew_mean      | 1.33     |
|    exploration_rate | 0.781    |
| time/               |          |
|    episodes         | 12       |
|    fps              | 15       |
|    time_elapsed     | 150      |
|    total_timesteps  | 2306     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.000121 |
|    n_updates        | 551      |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 188      |
|    ep_rew_mean      | 1.25     |
|    exploration_rate | 0.714    |
| time/               |          |
|    episodes         | 16       |
|    fps              | 16       |
|    time_elapsed     | 178      |
|    total_timesteps  | 3010     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.000167 |
|    n_updates        | 727      |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 192      |
|    ep_rew_mean      | 1.4      |
|    exploration_rate | 0.635    |
| time/               |          |
|    episodes         | 20       |
|    fps              | 16       |
|    time_elapsed     | 231      |
|    total_timesteps  | 3842     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 8.91e-05 |
|    n_updates        | 935      |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 198      |
|    ep_rew_mean      | 1.5      |
|    exploration_rate | 0.55     |
| time/               |          |
|    episodes         | 24       |
|    fps              | 16       |
|    time_elapsed     | 282      |
|    total_timesteps  | 4741     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 4.27e-05 |
|    n_updates        | 1160     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 202      |
|    ep_rew_mean      | 1.61     |
|    exploration_rate | 0.462    |
| time/               |          |
|    episodes         | 28       |
|    fps              | 18       |
|    time_elapsed     | 306      |
|    total_timesteps  | 5665     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.0054   |
|    n_updates        | 1391     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 201      |
|    ep_rew_mean      | 1.56     |
|    exploration_rate | 0.389    |
| time/               |          |
|    episodes         | 32       |
|    fps              | 19       |
|    time_elapsed     | 323      |
|    total_timesteps  | 6428     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.000104 |
|    n_updates        | 1581     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 201      |
|    ep_rew_mean      | 1.58     |
|    exploration_rate | 0.312    |
| time/               |          |
|    episodes         | 36       |
|    fps              | 21       |
|    time_elapsed     | 342      |
|    total_timesteps  | 7246     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 7.45e-05 |
|    n_updates        | 1786     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 199      |
|    ep_rew_mean      | 1.5      |
|    exploration_rate | 0.242    |
| time/               |          |
|    episodes         | 40       |
|    fps              | 22       |
|    time_elapsed     | 360      |
|    total_timesteps  | 7977     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.0001   |
|    n_updates        | 1969     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 203      |
|    ep_rew_mean      | 1.52     |
|    exploration_rate | 0.151    |
| time/               |          |
|    episodes         | 44       |
|    fps              | 23       |
|    time_elapsed     | 384      |
|    total_timesteps  | 8942     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 7.86e-05 |
|    n_updates        | 2210     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 207      |
|    ep_rew_mean      | 1.52     |
|    exploration_rate | 0.0579   |
| time/               |          |
|    episodes         | 48       |
|    fps              | 24       |
|    time_elapsed     | 409      |
|    total_timesteps  | 9917     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.000115 |
|    n_updates        | 2454     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 212      |
|    ep_rew_mean      | 1.48     |
|    exploration_rate | 0.05     |
| time/               |          |
|    episodes         | 52       |
|    fps              | 25       |
|    time_elapsed     | 436      |
|    total_timesteps  | 11038    |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.0003   |
|    n_updates        | 2734     |
----------------------------------
----------------------------------
| rollout/            |          |
|    ep_len_mean      | 213      |
|    ep_rew_mean      | 1.54     |
|    exploration_rate | 0.05     |
| time/               |          |
|    episodes         | 56       |
|    fps              | 25       |
|    time_elapsed     | 459      |
|    total_timesteps  | 11946    |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0.000394 |
|    n_updates        | 2961     |
----------------------------------
Killed
```
