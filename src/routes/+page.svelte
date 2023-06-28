<script>
	import { register } from 'swiper/element/bundle';
	import { onMount } from 'svelte';

	register();

	const spaceBetween = 10;
	const onProgress = (e) => {
		const [swiper, progress] = e.detail;
		console.log(progress);
	};
	const onSlideChange = (e) => {
		console.log('slide changed');
	};

    // swiper parameters
  const swiperParams = {
    slidesPerView: 1,
    pagination: {
        clickable: true
    },
    loop: true,
    // array with CSS styles
    injectStyles: [
      `
      .swiper-button-prev:after, .swiper-button-next:after {
        color: #FFF;
        font-size: 32px;
      }

      .swiper-pagination-bullet {
        background: #BEBEBE;
      }

      .swiper-pagination-bullet-active {
        background: #FFF;
      }
      `,
    ],
    on: {
      init() {
        // ...
      },
    },
  };

	onMount(() => {
        // swiper element
		const swiperEl = document.querySelector('swiper-container');
        if (swiperEl != null) {
            // now we need to assign all parameters to Swiper element
            Object.assign(swiperEl, swiperParams);

            // and now initialize it
            // @ts-ignore
            swiperEl.initialize();
        }
	});
</script>

<section class="header">
	<div class="start" />
	<img src="/LOGO.png" alt="logo.png" />
    <a class="end" href="https://github.com/leminhyen2/Sugoi-Japanese-Translator" target="_blank">
        <button class="button">
            <p>GitHub</p>
            <i class="bi bi-github" />
        </button>
    </a>
</section>

<section class="hero">
	<!-- <img src="/hero.svg" alt="hero.svg"/> -->
	<h1>Sugoi Translator Toolkit</h1>
	<p>Translate all Japanese entertainment with just one program.</p>
</section>

<div class="divider" />

<section class="features">
	<div id="feature-1">
		<div class="feature-image">
			<lottie-player
				src="/sugoi_translator_feature1.json"
				background="transparent"
				speed="0.5"
				loop
				autoplay
			/>
		</div>
		<div class="text-group">
			<h3>Translate everything with ease</h3>
			<p>
				Need help understanding raw manga, untranslated visual novels, ASMR clips, or Japanese light
				novel? Sugoi Toolkit is here tol help you!
			</p>
		</div>
	</div>
	<div id="feature-2">
		<div class="text-group">
			<h3>Best translator for Japanese culture</h3>
			<p>
				Our Sugoi models have consistently beat out DeepL and Google on visual novel, manga, light
				novel benchmarks (BLEU score).
			</p>
		</div>
		<div class="table">
			<table>
				<tr>
					<th><h6>Name</h6></th>
					<th><h6>Total</h6></th>
					<th><h6>{@html 'Visual Novel:\nHarmonia'}</h6></th>
					<th><h6>{@html 'Manga:\nOpen Mantra Dataset'}</h6></th>
					<th><h6>{@html 'Light Novel:\nItachi Shinden'}</h6></th>
				</tr>
				<tr>
					<td><p>Sugoi Translator V4</p></td>
					<td><p>58.81</p></td>
					<td><p>20.77</p></td>
					<td><p>21</p></td>
					<td><p>17.02</p></td>
				</tr>
				<tr>
					<td><p>Sugoi Translator V3</p></td>
					<td><p>54.59</p></td>
					<td><p>19.43</p></td>
					<td><p>20.74</p></td>
					<td><p>14.42</p></td>
				</tr>
				<tr>
					<td><p>DeepL</p></td>
					<td><p>53.96</p></td>
					<td><p>19.08</p></td>
					<td><p>20.59</p></td>
					<td><p>14.29</p></td>
				</tr>
				<tr>
					<td><p>Sugoi Translator V2</p></td>
					<td><p>50.68</p></td>
					<td><p>18.75</p></td>
					<td><p>19.66</p></td>
					<td><p>12.27</p></td>
				</tr>
				<tr>
					<td><p>Papago</p></td>
					<td><p>47.43</p></td>
					<td><p>18.01</p></td>
					<td><p>18.36</p></td>
					<td><p>11.06</p></td>
				</tr>
				<tr>
					<td><p>Sugoi Translator V1</p></td>
					<td><p>46.83</p></td>
					<td><p>18.29</p></td>
					<td><p>17.16</p></td>
					<td><p>11.38</p></td>
				</tr>
				<tr>
					<td><p>Google</p></td>
					<td><p>46.57</p></td>
					<td><p>17.94</p></td>
					<td><p>16.07</p></td>
					<td><p>12.56</p></td>
				</tr>
			</table>
		</div>
	</div>
	<div id="feature-3">
		<div class="text-group">
			<h3>Work 100% offline</h3>
			<p>
				Whether you're at home or travelling on airplane, Sugoi Toolkit will reliably translate your
				content.
			</p>
		</div>
		<div class="feature-image">
			<img src="/feature3.svg" alt="feature3.svg" />
		</div>
	</div>
	<div id="feature-4">
		<div class="text-group">
			<h3>Real-time Translation</h3>
			<p>
				Accelerate translation to subsecond speed with your local GPU or with our online servers.
			</p>
		</div>
		<div class="table">
			<table>
				<tr>
					<th><h6>Region</h6></th>
					<th><h6>Server</h6></th>
					<th><h6>Short Texts (s)</h6></th>
					<th><h6>Medium Texts (s)</h6></th>
					<th><h6>Long Texts (s)</h6></th>
					<th><h6>Average Speed (s)</h6></th>
				</tr>
				<tr>
					<td><p>Local</p></td>
					<td><p>GPU</p></td>
					<td><p>0.07</p></td>
					<td><p>0.17</p></td>
					<td><p>0.24</p></td>
					<td><p>10.16</p></td>
				</tr>
				<tr>
					<td><p>USA</p></td>
					<td><p>California</p></td>
					<td><p>0.19</p></td>
					<td><p>0.26</p></td>
					<td><p>0.34</p></td>
					<td><p>0.26</p></td>
				</tr>
				<tr>
					<td><p>USA</p></td>
					<td><p>Ohio</p></td>
					<td><p>0.34</p></td>
					<td><p>0.37</p></td>
					<td><p>0.43</p></td>
					<td><p>0.38</p></td>
				</tr>
				<tr>
					<td><p>Europe</p></td>
					<td><p>Finland</p></td>
					<td><p>0.39</p></td>
					<td><p>0.47</p></td>
					<td><p>0.55</p></td>
					<td><p>0.47</p></td>
				</tr>
				<tr>
					<td><p>Europe</p></td>
					<td><p>Spain</p></td>
					<td><p>0.47</p></td>
					<td><p>0.62</p></td>
					<td><p>0.66</p></td>
					<td><p>0.58</p></td>
				</tr>
				<tr>
					<td><p>Asia</p></td>
					<td><p>Vietnam</p></td>
					<td><p>0.44</p></td>
					<td><p>0.54</p></td>
					<td><p>0.65</p></td>
					<td><p>0.54</p></td>
				</tr>
				<tr>
					<td><p>Asia</p></td>
					<td><p>Malaysia</p></td>
					<td><p>0.56</p></td>
					<td><p>0.66</p></td>
					<td><p>0.75</p></td>
					<td><p>0.66</p></td>
				</tr>
				<tr>
					<td><p>Local</p></td>
					<td><p>i5 9th CPU</p></td>
					<td><p>0.46</p></td>
					<td><p>1.4</p></td>
					<td><p>2.1</p></td>
					<td><p>1.32</p></td>
				</tr>
			</table>
		</div>
	</div>
</section>

<div class="divider-top" />

<section class="numbers">
	<div class="text-group">
		<h3>Trusted by many</h3>
		<p>
			Sugoi Translator has been tested by countless users, and we’ve got the numbers to prove it.
		</p>
	</div>
	<div class="number-list">
		<div class="number-item">
			<i class="bi bi-discord" />
			<div class="text-group">
				<h2>>6,000</h2>
				<h5>Discord members</h5>
			</div>
		</div>
		<div class="number-item">
			<i class="bi bi-people-fill" />
			<div class="text-group">
				<h2>>13,000</h2>
				<h5>weekly users</h5>
			</div>
		</div>
		<div class="number-item">
			<i class="bi bi-youtube" />
			<div class="text-group">
				<h2>>230,000</h2>
				<h5>views on Youtube</h5>
			</div>
		</div>
	</div>
</section>

<section class="testimonials">
	<div class="text-group">
		<h3>Testimonials</h3>
		<p>Hear from our satisfied customers.</p>
	</div>
	<swiper-container
        init="false"
		slides-per-view={1}
		space-between={spaceBetween}
		centered-slides={true}
		navigation="true"
		pagination="true"
		on:progress={onProgress}
		on:slidechange={onSlideChange}
	>
		<swiper-slide>
            <div class="slide-content">
                <i class="bi bi-quote"></i>
                <p>
                    hi just wanted to let anyone who helped and made VNO OCR is amazing thank you sooo much because back then I used VNR and it worked pretty well until eventually I tried all solutions but wasn't able to start it up anymore even when downloading the new version I was really frustrated cause I couldn't play the visual novels that I wanted to play/continue but I just wanted to say I'm really grateful to the person who made VNO this is amazing thank you sooo much!!

                    - Rynx, 2021
                </p>
                <i class="bi bi-quote" style="transform: scaleX(-1)"></i>
            </div>
        </swiper-slide>
		<swiper-slide>
            <div class="slide-content">
                <i class="bi bi-quote"></i>
                <p>
                    Even so, any level of accuracy increase is amazing. The fact that you are a solo developer who has put together a package that is able to translate VN/Manga Japanese as accurately as DeepL is pretty astounding. I can basically read stuff now that has 0 chance of ever being translated. I've tried machine translations in the past but they were basically unreadable, they literally gave me a headache, but with your program I can actually read this stuff with no issues lol.

                    - MasterBlaster, 2021
                </p>
                <i class="bi bi-quote" style="transform: scaleX(-1)"></i>
            </div>
        </swiper-slide>
		<swiper-slide>
            <div class="slide-content">
                <i class="bi bi-quote"></i>
                <p>
                    Tbf I had been looking for a tool like Sugoi for years until I finally found it in a vague reddit thread... It was like finding a needle in a haystack.

                    - TheDemonGallows, 2023
                </p>
                <i class="bi bi-quote" style="transform: scaleX(-1)"></i>
            </div>
        </swiper-slide>
	</swiper-container>
</section>

<div class="divider" />

<section class="footer">
	<img src="/LOGO-blue.png" alt="logo.png" />
	<p>Copyright 2023. Sugoi Translator Inc.</p>
</section>

<style lang="scss">
	@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css');

	$black100: #121212;
	$black50: #888888;
	$black25: #bebebe;
	$primary_blue: #099be5;
	$dark_blue: #414ba2;
	$brown: #68382f;
	$primary_orange: #fba830;
	$faded_orange: #f9ae5d;
	$pale_yellow: #fce5a8;
	$salmon: #f58a8f;
	$white: #ffffff;

	// Global
	section {
		padding: 32px;
	}

	.button {
		display: flex;
		gap: 8px;
		justify-content: center;
		align-items: center;

		border-radius: 1000px;
		padding: 8px 32px;
		width: max-content;

		background: $white;
		border: 2px solid $primary_blue;

		&:hover {
			border: 2px solid $dark_blue;
		}

		i {
			font-size: 16px;
		}
	}

	// .filled-button {
	// 	background-color: $primary_blue;

	// 	&:hover {
	// 		background: $dark_blue;
	// 	}
	// }

	.start {
		justify-self: start;
	}
	.end {
		justify-self: end;
	}

	.text-group {
		display: flex;
		flex-direction: column;
		gap: 12px;
	}

	// Divider
	.divider {
		background: $white;
		background-image: url(/divider.svg);
		background-size: cover;
		height: 48px;
	}
	.divider-top {
		background: $white;
		background-image: url(/divider-top.svg);
		background-size: cover;
		height: 48px;
	}

	// Header
	.header {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		justify-items: center;
		align-items: center;

		img {
			height: 60px;
		}

		// position: sticky;
		// top: 0;
		// z-index: 1000;
		// background: linear-gradient($primary_blue, transparent);
	}

	// Hero
	.hero {
		display: flex;
		flex-direction: column;
		gap: 12px;
		justify-content: center;

        background-image: url(/hero-mobile.svg);
		background-position: center;
		background-size: contain;
		background-repeat: no-repeat;
		height: 360px;

		color: $white;

        @media screen and (min-width: 426px) {
            background-image: url(/hero-tablet2.svg);
        }

        @media screen and (min-width: 769px) {
            background-image: url(/hero-tablet1.svg);
        }

        @media screen and (min-width: 1025px) {
            align-items: center;
            background-image: url(/hero.svg);
        }
	}

	// Features
	.features {
		background: $white;

		display: flex;
		flex-direction: column;
		gap: 64px;

		#feature-1,
		#feature-3 {
			display: flex;
			flex-wrap: wrap;
			gap: 32px;
			justify-content: center;
			align-items: center;

			.text-group {
				flex: 1 1 450px;
			}

			.feature-image {
				max-width: 450px;

				lottie-player,
				img {
					width: 100%;
				}
			}
		}

		@media screen and (max-width: 995px) {
			#feature-1 {
				.feature-image {
					order: 1;
				}
			}
		}

		@media screen and (min-width: 996px) {
			#feature-1,
			#feature-3 {
				.text-group {
					max-width: 450px;
				}
			}
		}

		#feature-2,
		#feature-4 {
			display: flex;
			flex-direction: column;
			justify-content: center;
			gap: 24px;
		}
		@media screen and (min-width: 996px) {
			#feature-2,
			#feature-4 {
				align-items: center;

				h3,
				p {
					text-align: center;
				}
			}
		}
	}

	.table {
		width: fit-content;
		@media screen and (max-width: 995px) {
			width: 100%;
		}

		overflow-x: scroll;
		-webkit-overflow-scrolling: touch;

		&::-webkit-scrollbar {
			height: 44px;
		}

		&::-webkit-scrollbar-thumb {
			background: $faded_orange;
			border-radius: 1000px;
			border: 20px solid rgba(0, 0, 0, 0);
			background-clip: padding-box;
		}

		table {
			border-spacing: 12px;
			th,
			td {
				padding: 16px 32px;
				border-radius: 8px;
			}

			tr:nth-child(odd) {
				background: $pale_yellow;
			}

			tr:nth-child(even) {
				th,
				td {
					border: solid 1px $black25;
				}
			}

			tr:nth-child(1) {
				background: $white;
			}
		}

		h6,
		p {
			text-align: center;
		}
	}

	#feature-2 .table table {
		tr:nth-child(2) {
			background: $primary_blue;
			th,
			td {
				border: none;
				color: $white;
				p {
					font-weight: bold;
				}
			}
		}
	}

	#feature-4 .table table tr {
		th:last-child {
			position: sticky;
			right: 0;
			background: $dark_blue;
			color: $white;
		}

		td:last-child {
			position: sticky;
			right: 0;
			background: $primary_blue;
			border: none;
			color: $white;
			p {
				font-weight: bold;
			}
		}
	}

	// Numbers
	@media screen and (min-width: 996px) {
		.numbers {
			align-items: center;

			h3,
			p {
				text-align: center;
			}
		}
	}

	.numbers {
		color: $white;

		display: flex;
		flex-direction: column;
		justify-content: center;
		gap: 24px;

		.number-list {
			display: grid;
			gap: 24px;
			overflow-x: auto;
			grid-auto-flow: column;
			overscroll-behavior-x: auto;
			scroll-snap-type: x mandatory;
			-webkit-overflow-scrolling: touch;

			&::-webkit-scrollbar {
				height: 44px;
			}

			&::-webkit-scrollbar-thumb {
				background: $dark_blue;
				border-radius: 1000px;
				border: 20px solid rgba(0, 0, 0, 0);
				background-clip: padding-box;
			}
		}

		.number-item {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			gap: 20px;

			background: $white;
			color: $dark_blue;
			border-radius: 8px;
			padding: 48px 48px;

			min-width: 200px;
			max-width: 300px;
			scroll-snap-align: center;

			i {
				font-size: 120px;
			}

			h2,
			h5 {
				text-align: center;
			}
		}
	}

	// Testimonials
	@media screen and (min-width: 996px) {
		.testimonials {
			align-items: center;

			h3,
			p {
				text-align: center;
			}
		}
	}

	.testimonials {
		color: $white;

		display: flex;
		flex-direction: column;
		justify-content: center;
		gap: 24px;
	}

    swiper-container {
        width: 100%;
        display: grid;
        max-width: 996px;
    }

    swiper-slide {
        display: grid;
        place-items: center;
    }

    .slide-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        max-width: 996px;
        padding: 0 64px;
        margin: auto;

        i {
            font-size: 64px;
        }

        i:first-child {
            align-self: flex-start;
        }
        i:last-child {
            align-self: flex-end;
        }
    }

	// Footer
	.footer {
		background: $white;

		display: grid;
		place-items: center;
		gap: 12px;

		img {
			height: 90px;
		}
	}
</style>
