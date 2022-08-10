<template>
  <HeaderBar/>

  <p>Hazardest has no advertisements, is not sponsored, and provides its services free of charge. For these reasons,
    Hazardest's financial obligations can only be met with the help of voluntary user donations. Supporting Hazardest is
    and will always remain voluntary. If you are financially able, help pay Hazardest's bills by donating. Hazardest's
    survival is up to you.</p>

  <p>Hazardest uses all voluntary donations to cover the costs of running the site, tracker, and IRC network. These
    costs represent the hardware the site runs on (e.g., servers, upgrades, fixes, etc.), and recurring operating
    expenses (e.g., hosting, bandwidth, power, etc.).</p>

  <p>Please note that Hazardest is a nonprofit organization. No staff member or other individual responsible for the
    site's operation personally profits from user donations. As a donor, your financial support is exclusively applied
    to operating costs. When you donate you aren't paying the Hazardest Staff, purchasing upload credit, or buying the
    ability to download. When you donate you are paying Hazardest's bills.</p>

  <p>Hazardest's Donor Rank system is currently available to all credited donors. This system provides donors with
    perks. Some of these perks are cosmetic (e.g., a donor icon added to your account), some are one-time benefits
    (e.g., additional invites), and others modify specific site options (e.g., additional profile information boxes, or
    personal collages).</p>

  <a href="https://square.link/u/OmK3biCX">Donate</a>


  <div>
    <div>
      <div style="
  overflow: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  width: 259px;
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: -2px 10px 5px rgba(0, 0, 0, 0);
  border-radius: 10px;
  font-family: SQ Market, Helvetica, Arial, sans-serif;
  ">
        <div style="padding: 20px;">
          <a target="_blank" data-url="https://square.link/u/qrHoyLzE?src=embd"
             href="https://square.link/u/qrHoyLzE?src=embed" style="
    display: inline-block;
    font-size: 18px;
    line-height: 48px;
    height: 48px;
    color: #ffffff;
    min-width: 212px;
    background-color: #000000;
    text-align: center;
    box-shadow: 0 0 0 1px rgba(0,0,0,.1) inset;

  ">Donate</a>
        </div>
      </div>
    </div>

  </div>


  <FooterBar/>

</template>

<script>
import HeaderBar from "@/components/trim/HeaderBar";
import FooterBar from "@/components/trim/FooterBar";

export default {
  name: "DonateHazardest",
  components: {
    HeaderBar,
    FooterBar
  }

}


// square button
     function showCheckoutWindow(e) {
        e.preventDefault();

        const url = document.getElementById('embedded-checkout-modal-checkout-button').getAttribute('data-url');
        const title = 'Square Online Checkout';

        // Some platforms embed in an iframe, so we want to top window to calculate sizes correctly
        const topWindow = window.top ? window.top : window;

        // Fixes dual-screen position                                Most browsers          Firefox
        const dualScreenLeft = topWindow.screenLeft !== undefined ? topWindow.screenLeft : topWindow.screenX;
        const dualScreenTop = topWindow.screenTop !== undefined ? topWindow.screenTop : topWindow.screenY;

        const width = topWindow.innerWidth ? topWindow.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
        const height = topWindow.innerHeight ? topWindow.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;

        const h = height * .75;
        const w = 500;

        const systemZoom = width / topWindow.screen.availWidth;
        const left = (width - w) / 2 / systemZoom + dualScreenLeft;
        const top = (height - h) / 2 / systemZoom + dualScreenTop;
        const newWindow = window.open(url, title, `scrollbars=yes, width=${w / systemZoom}, height=${h / systemZoom}, top=${top}, left=${left}`);

        if (window.focus) newWindow.focus();
      }

      // This overrides the default checkout button click handler to show the embed modal
      // instead of opening a new tab with the given link url
      document.getElementById('embedded-checkout-modal-checkout-button').addEventListener('click', function (e) {
        showCheckoutWindow(e);
      });
</script>

<style scoped>

</style>