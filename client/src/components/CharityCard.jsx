import React from 'react';
import '../App.css';

function CharityCard({ title, description, donateLink }) {
  return (
    <div
  class="block max-w-[18rem] rounded-lg bg-white text-surface shadow-secondary-1 dark:bg-surface-dark dark:text-white">
  <div class="relative overflow-hidden bg-cover bg-no-repeat">
    <img
      class="rounded-t-lg"
      src="https://tecdn.b-cdn.net/img/new/standard/nature/182.jpg"
      alt="" />
  </div>
  <div class="p-6">
    <p class="text-base">
      Some quick example text to build on the card title and make up the
      bulk of the card's content.
    </p>
    <button
      type="button"
      href="#"
      class="inline-block rounded bg-primary px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-primary-3 transition duration-150 ease-in-out hover:bg-primary-accent-300 hover:shadow-primary-2 focus:bg-primary-accent-300 focus:shadow-primary-2 focus:outline-none focus:ring-0 active:bg-primary-600 active:shadow-primary-2 dark:shadow-black/30 dark:hover:shadow-dark-strong dark:focus:shadow-dark-strong dark:active:shadow-dark-strong"
      data-twe-ripple-init
      data-twe-ripple-color="light">
      Donate Now
    </button>
  </div>
</div>
  );
}

export default CharityCard;